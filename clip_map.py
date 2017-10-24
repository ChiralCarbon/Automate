import webbrowser as wb 
import clipboard 
clip_text=clipboard.paste()
url='https://www.google.co.in/maps/place/'
url_extend='+'.join(clip_text.split(' '))
url=url+url_extend
wb.open(url)