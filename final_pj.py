from lxml import html
import requests
import mechanize

page = html.parse('http://registrar.ucsc.edu/catalog/programs-courses/course-descriptions/art.html')
li_ists = page.xpath('//*[@id="subNav"]/ul/li[14]/ul/li[3]/ul/*')
major_list = []
major_link_a_list = []
all_data = []
count = 0
# major_abbr_list = []
all_subject = ['ACEN', 'AMST', 'ANTH', 'APLX', 'AMS', 'ARAB', 'ART', 'ARTG', 'ASTR', 'BIOC', 'BIOL', 'BIOE', 'BME',
               'CRSN', 'CHEM', 'CHIN', 'CLEI', 'CLNI', 'CLTE', 'CMMU', 'CMPM', 'CMPE', 'CMPS', 'COWL', 'LTCR', 'CRES',
               'CRWN', 'DANM', 'EART', 'ECON', 'EDUC', 'EE', 'ENGR', 'LTEL', 'ENVS', 'ETOX', 'FMST', 'FILM', 'FREN',
               'LTFR', 'GAME', 'GERM', 'LTGE', 'GREE', 'LTGR', 'HEBR', 'HNDI', 'HIS', 'HAVC', 'HISC', 'HUMN', 'ISM',
               'ITAL', 'LTIT', 'JAPN', 'JWST', 'KRSG', 'LAAD', 'LATN', 'LALS', 'LTIN', 'LGST', 'LING', 'LIT', 'MATH',
               'MERR', 'METX', 'LTMO', 'MUSC', 'OAKS', 'OCEA', 'PHIL', 'PHYE', 'PHYS', 'POLI', 'PRTR', 'PORT', 'LTPR',
               'PSYC', 'PUNJ', 'RUSS', 'SCIC', 'SOCD', 'SOCS', 'SOCY', 'SPAN', 'SPHS', 'SPSS', 'LTSP', 'STEV', 'TIM',
               'THEA', 'UCDC', 'WMST', 'LTWL', 'WRIT', 'YIDD']
# len(all_subject) = 97


br = mechanize.Browser()
br.open("https://pisa.ucsc.edu/cs9/prd/sr9_2013/index.php")

for li in li_ists:
    major_list.append(li.xpath('./a/@href'))
for i in range(len(major_list)):
    major_link_a_list.append(major_list[i][0])  # creat a list to store  the link appendix of a major, ex: cmps.html

for i in range(len(major_link_a_list)):
    major_link_a = major_link_a_list[i]
    base_url = 'http://registrar.ucsc.edu/catalog/programs-courses/course-descriptions/'
    major_link = requests.get(base_url + major_link_a)
    aa = str(major_link_a)
    bb = aa.replace('.html', '')
    major_abbr = bb.upper()

    if major_abbr in ['CLST', 'EEB', 'MCDB']:
        continue  # CLST, EEB, MCDB which show up in base_url are not in all_subject
    # major_abbr_list.append(major_abbr)
    # len(major_abbr_list)=76
    class_of_the_subject = {}

    class_num_list = []
    major_page = html.parse(major_link.url)
    class_list_1 = major_page.xpath('//*[@class="content contentBox"]/*')
    subject = major_page.xpath('//*[@id="title"]')[0].text_content()
    for class_element in class_list_1:
        if len(class_element.xpath('strong')) > 0:
            class_num_list.append(class_element.xpath('strong')[0].text_content().replace('.', ''))
    # print class_num_list

    for ii in range(len(class_num_list)):
        class_number = class_num_list[ii]
        try:
            br.select_form('searchForm')
            br.form['binds[:term]'] = ['2172', ]
            br.form['binds[:reg_status]'] = ['all', ]
            br.form['binds[:subject]'] = [major_abbr, ]
            br.form['binds[:catalog_nbr]'] = class_number
            response = br.submit()
            page = html.document_fromstring(response.read())

            class_list_2 = page.xpath('//div[@class="panel panel-default row"]')
            if class_list_2 == []:
                continue
            class_of_the_subject['Subject'] = subject
            class_of_the_subject['Class_Number'] = major_abbr + class_number
            class_of_the_subject['Class_name'] = page.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/h2/a[2]')[
                0].text_content()
            class_of_the_subject['Instructor'] = page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/text()')[
                0]
            class_of_the_subject['Capacity'] = page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[5]')[
                0].text_content()
            class_of_the_subject['Day_And_Time'] = \
                page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[4]/text()')[0]
            class_of_the_subject['Class_Location'] = \
                page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[3]/text()')[0]
            all_data.append(class_of_the_subject)
            count += 1

        except:
            print "This is an error message!"
        break

print all_data
print count
