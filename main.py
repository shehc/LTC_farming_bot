import colorama
import re
import time
from selenium import webdriver
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from colorama import Fore
import undetected_chromedriver.v2 as uc


colorama.init()

api_id = "Your api_id"
api_hash = 'Your api_hash'
client = TelegramClient('anon', api_id, api_hash)
username = '@Litecoin_click_bot'

url_pattern = r'https?://dog\S+' # filter for link search
message_bot_pattern = '/html/body/div[1]/div[2]/div[3]'
join_bot_pattern = '/html/head/title'

"""Bot for surfing"""
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
async def check():# Captcha checking or CloudFlare
	text_cloudflare = await client.get_messages(username, limit = 1) # pulling text
	check_cloudflare = re.findall(r'Please stay on the site for at least', str(text_cloudflare)) # checking for this text
	
	if str(check_cloudflare) == "['Please stay on the site for at least']":
		time.sleep(10)
		print(Fore.GREEN + 'Surfing task completed!')
	else:
		time.sleep(1)
		await text_cloudflare[0].click(2)
		print(Fore.RED + 'Captcha!')
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
async def surf_browser(url):# browser configuration
	options = uc.ChromeOptions()
	options.headless = True
	options.add_argument('window-size=10,10')
	browser = uc.Chrome(options=options)
	try:
		browser.get(url)
		browser.close()
		browser.quit()
	except:
		print('\n')
	await check()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////	
async def surf_bot():
		stop_while = True
		while stop_while:
			time.sleep(1)
			await client.send_message(username, '🖥 Visit sites') # making a mission request
			time.sleep(3)
			
			text = await client.get_messages(username,  limit = 1) # pulling text with a link
			time.sleep(1)

			if re.findall('https://dog', str(text)) or re.findall('http://dog', str(text)):
				url = re.findall(url_pattern, str(text)) # pulling part of the link
				get_url = url[0][:len(url) - 6]	# formatting the link
				await surf_browser(get_url) 
			else:
				print(Fore.WHITE + 'There are no surfing tasks!')
				time.sleep(1)
				stop_while = False
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""Bot for message"""
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
async def join_and_message_bot_browser(bot_get_url, bot_pattern):
	options = uc.ChromeOptions()
	options.headless = True
	options.add_argument('window-size=50,50')
	browser = uc.Chrome(options=options)
	browser.get(bot_get_url)
	message_bot_username = browser.find_element_by_xpath(bot_pattern).get_attribute("innerHTML")
	browser.close()
	browser.quit()
	return message_bot_username
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////	
async def  message_bot():
	while True:
		time.sleep(3)
		await client.send_message(username, '🤖 Message bots')
		time.sleep(2)
			
		ms_bot_text = await client.get_messages(username, limit = 1)
		time.sleep(1)
		
		'''Checking for tasks.'''
		if re.findall('https://dog', str(ms_bot_text)) or re.findall('http://dog', str(ms_bot_text)):
			ms_bot_url = re.findall(url_pattern, str(ms_bot_text)) # pulling part of the link
			ms_bot_get_url = ms_bot_url[0][:len(ms_bot_url) - 6]	# formatting the link
			time.sleep(1)
			try:
				'''Pulling the bot's nickname..'''
				bot_username = await join_and_message_bot_browser(ms_bot_get_url, message_bot_pattern)
				print(bot_username)
				time.sleep(1)
				await client.send_message(bot_username, '/start')
				time.sleep(10)
				bot_text = await client.get_messages(username, limit = 1)

				
				'''Checking the bot for validity.'''
				if  re.findall('/start', str(bot_text)):
					print(asdqweqwqasdasasd)
				else:
					'''Pulling the id of the message sent by the bot..'''
					text_msg_bot_id = await client.get_messages(bot_username)
					find_msg_bot_id = re.findall(r'id=\d+',str(text_msg_bot_id))
					msg_bot_id = re.findall(r'\d+', find_msg_bot_id[0])[0]
					print(Fore.GREEN + 'Forwarding task completed!')
					time.sleep(1)
					
					await client.forward_messages(username, int(msg_bot_id), bot_username)
			except Exception as err:
				print(err)
				print(Fore.RED + 'CloudFlare or invalid url!')
				time.sleep(1)
				await ms_bot_text[0].click(2)
				time.sleep(1)
				continue
		else:
			print(Fore.WHITE + 'No forwarding tasks!')
			time.sleep(1)
			break
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
async def join_bot():
	end_of_cycle = 0
	while True:
		time.sleep(2)
		await client.send_message(username, '/join') 
		time.sleep(3)
		j_bot_text = await client.get_messages(username, limit = 1)
		time.sleep(1)
			
		'''Checking for tasks.'''
		if re.findall('https://dog', str(j_bot_text)) or re.findall('http://dog', str(j_bot_text)):
			try:
				'''Pulling up the link'''
				j_bot_url = re.findall(url_pattern, str(j_bot_text)) # pulling part of the link
				j_bot_get_url = j_bot_url[0][:len(j_bot_url) - 4]	# formatting the link
				time.sleep(1)

				'''Pulling up the channel username'''
				text_bot_username = await join_and_message_bot_browser(j_bot_get_url, join_bot_pattern)
				join_bot_username = re.findall(r'@\S+', text_bot_username)[0]
				print(join_bot_username)
				time.sleep(2)

				'''Join the channel'''
				await client(JoinChannelRequest(join_bot_username))
				time.sleep(2)

				'''Click on the task check button'''
				await j_bot_text[0].click(1)

				print(Fore.GREEN + 'Task to join completed!')

				end_of_cycle += 1
				if end_of_cycle > 30:
					time.sleep(1800)
					break
			except Exception as err:
				print(err)
				print(Fore.RED + 'CloudFlare or invalid url!')
				time.sleep(1)
				await j_bot_text[0].click(3)
					
				end_of_cycle += 1
				if end_of_cycle > 30:
					time.sleep(1800)
					break	

				continue	
		else:
			print(Fore.WHITE + 'No tasks to join!')
			break
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
async def main():
	cycle_number = 0
	while True:
		print(Fore.CYAN + 'Going to surf_bot.\n')
		time.sleep(3)

		await surf_bot()
		
		print(Fore.CYAN + '\nGoing to message_bot.\n')
		time.sleep(3)
		
		await message_bot()

	#	print(Fore.CYAN + '\nGoing to join_bot.\n')
	#	time.sleep(3)
		
	#	await join_bot()

		cycle_number += 1
		print(Fore.MAGENTA + '\nCycle № ' + str(cycle_number) + ' complete.', 'Going to the next account.\n')
		time.sleep(3)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
with client:
    client.loop.run_until_complete(main())

