from DrissionPage import ChromiumPage, ChromiumOptions
co = ChromiumOptions().set_browser_path(r"D:\Program Files\Google\Chrome\Application\chrome.exe")
page = ChromiumPage(addr_or_opts=co)
tab = page.new_tab()
tab.get('https://dash.cloudflare.com/login')
tab.wait(8,10)
ll = tab.ele('x://div[@class="c_cq"]/div/div').shadow_root.ele("@tag()=iframe").ele('x://body').shadow_root.ele('x://input').click()
if ll:
    print("CF验证成功")
else:
    print("CF验证失败")