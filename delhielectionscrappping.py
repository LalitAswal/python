from requests import get


          



                                                  #print(elction_commission)
                                                  #print(len(elction_commission))
Constituency=[]
Leading_Candidate=[]
Leading_Party=[]
Margin=[]
Trailing_Candidate=[]
Trailing_Party=[]
for i in range(1,7):
          url='http://results.eci.gov.in/DELHITRENDS2020/statewiseU05'+str(i)+'.htm'       
          response = get(url)
          from bs4 import BeautifulSoup

          html_soup = BeautifulSoup(response.text, 'html.parser')


          elction_commission=html_soup.find_all('tr',style="font-size:12px;")


          for container in elction_commission:
                    constituency=container.td.text
                    Constituency.append(constituency)
                    leading_Candidate=container.find_all('td')
                    Leading_Candidate.append(leading_Candidate[2].text.strip())
                    leading_Party=container.tr.td.text
                    Leading_Party.append(leading_Party)
                    margin=container.find_all('td',align='right')
                    Margin.append(margin[0].text.strip())
                    trailing_Candidate=container.find_all('td',align='left')
                    Trailing_Candidate.append(trailing_Candidate[3].text.strip())
                    
                    trailing_Party=container.find_all('td')
                    Trailing_Party.append(trailing_Party[4].text.strip())
#print(Constituency)
#print(Leading_Candidate)
#print(Leading_Party)
#print(Margin)         


import pandas as pd
data={'Constituency':Constituency,
          'Leading Candidate':Leading_Candidate,      
          'Leading Party':Leading_Party,
          'Margin':Margin,
      'Trailing Candidate':Trailing_Candidate,
      'Trailing Party':Trailing_Party
      }
#print(data)
test_df=pd.DataFrame(data)
print(test_df)
test_df.to_csv(r'C:\Users\aswal\Desktop\delhi_elction.csv',index=True)
                    
'''
          count=0
          bjp=0
          aap=0
          if Leading_Party=="Aam Aadmi Party":
                    count+=1
                    print('aap=',count)
                    
          elif Leading_Party=="Bharatiya Janata Party":
                    count+=1
                    
                    print('bjp=',count)
'''


