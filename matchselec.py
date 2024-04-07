import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

	
def match_suffix(d):
	total_data=[]	
	url="https://www.espncricinfo.com/live-cricket-match-schedule-fixtures"
	
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
	
	response=requests.get(url)
	if response.status_code==200:
		soup=bs(response.content, 'html.parser')
		f_soup=soup.find('div', class_='debug-fixture-date')
		#print(f_soup)
		fixture_date_data_items=f_soup.find_all('div', 'debug-fixture-date-item')
		print(len(fixture_date_data_items))
		#print(fixture_date_data_items[1])
		#Date selection
		x=0
		
		for item in fixture_date_data_items:
			#match_dict=[]
			date_soup= item.find('div', class_="ds-mb-6")
			#print(date_soup)
			date_soup=date_soup.find('div', class_="ds-flex ds-justify-center ds-mb-2")
			date=date_soup.find('span').get('id')
			date_with_day_name=date_soup.string
			print("\n"*2)
			x=x+1
			print(f'{x} . {date_with_day_name}')
			
			daywise_match_soups=item.find_all( 'a' , class_="ds-no-tap-higlight")
			for daywise_match_soup in daywise_match_soups:
				match_dict=[]
				match_dict.append(date_with_day_name)
				#d=daywise_match_soup.find('a', class_="ds-inline-flex ds-items-start ds-leading-none")
				#print(d)
		
				link_suffixs=daywise_match_soup.get('href')
				#print(link_suffixs)
				time_all=daywise_match_soup.find('div', class_="ds-flex-none ds-w-40")
				time=daywise_match_soup.find('span', class_="ds-text-compact-xs ds-font-bold ds-block ds--mb-1 ds-mt-[3px] ds-text-typo-mid1"). string 
				#print(time)				
				
				full_name_team=daywise_match_soup.find('p' , class_="ds-text-compact-s ds-font-bold ds--mb-1 ds-text-typo").text
				#print(full_name_team)
				details_all=daywise_match_soup.find('span', class_="ds-text-tight-xs ds-text-typo-mid3"). string
				#print(details_all)
				#print(match_dict)
				try:
					cover_it=daywise_match_soup.find('p', class_="ds-text-compact-xxs ds-font-medium ds-mt-1"). string 
					#print(cover_it)
				except:
					match_dict.append(time)
					match_dict.append(full_name_team)
					match_dict.append(details_all)
					match_dict.append(link_suffixs)
					#print(match_dict)
					total_data.append(match_dict)
	
	df=pd.DataFrame(data=total_data , columns=['date','time', 'match', 'details', 'link'])
	
	df=df[df.date==d]
	return df
	
	
						
