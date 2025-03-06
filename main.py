import re
import urllib
from time import sleep
from urllib.parse import urlparse
import httpx
from camoufox.sync_api import Camoufox

BASE_URL = "192.168.12.126:8111"

country = ""
single = set()

def add_link(link: str):
    print(link)
    with httpx.Client() as client:
        response = client.post(
            f"http://{BASE_URL}/TzsHsAFiR6cbH5EwSt2008X4Jt/add_link",
            json={"link": link, "country": country}
        )
        return response.json()

def process_stack(page):
    sleep(3)

    ad_count = int(page.get_by_text("个广告版本").text_content().replace("个广告版本", ""))
    subs_count = -1
    subs = None

    while ad_count > subs_count:
        subs = page.locator(
            "xpath=//div[@class='x1qjc9v5 x9f619 x78zum5 xdt5ytf x1nhvcw1 xg6iff7 xurb0ha x1sxyh0 x1l90r2v']//div[@class='xrvj5dj x18m771g x1amjocr xkj13zw xvg9xk2 x1jr1mh3']/*").all()
        subs_count = len(subs)
        page.mouse.wheel(0, 1000)

    page.mouse.wheel(0, -10000)

    sleep(1)

    for sub in subs:
        try:
            sub.get_by_text("查看广告详情").click(timeout=3000)
            process_details(page, False)
        except Exception as e:
            print(e)
            pass
    page.get_by_text("关闭").first.click()

def process_details(page, close):
    sleep(3)

    sub_page = page.locator(
        "xpath=//div[@class='x1qjc9v5 x9f619 x78zum5 xdt5ytf x1nhvcw1 xg6iff7 xurb0ha x1sxyh0 x1l90r2v']")


    extra = None
    try:
        # 展开按钮
        sub_page.locator(
            "xpath=//div[@class='x6s0dn4 x178xt8z x13fuv20 x15bcfbt x78zum5 x1q0g3np xyamay9 xxbr6pl x1l90r2v xbbxn1n']//div[@class='x3nfvp2 x120ccyz x1heor9g']").click(
            timeout=3000)
        sleep(1)
        extra = sub_page.locator("//div[@class='x1qjc9v5 x9f619 x78zum5 xdt5ytf x1nhvcw1 xg6iff7 xurb0ha x1sxyh0 x1l90r2v']//div[@class='x9otpla xqmxbcd x1yztbdb xmupa6y']//a").all()
    except Exception:
        pass

    links = sub_page.locator("xpath=//a").all()

    if extra:
        links.extend(extra)

    for link in links:
        href = link.get_attribute('href')  # 获取链接的 href 属性
        if href.startswith("http"):
            if href.startswith("https://l.facebook.com/"):
                href = extract_u_parameter(href)
            if filter(href):
                if href not in single:
                    single.add(href)
                    print(href)
                   # 测试阶段 add_link(href)

    if close:
        while True:
            try:
                sub_page.locator(
                    "xpath=//div[@class='x6s0dn4 x78zum5 x1q0g3np xozqiw3 x2lwn1j xeuugli x1iyjqo2 x19lwn94 x1hc1fzr x13dflua x6o7n8i xxziih7 x12w9bfk xl56j7k xh8yej3']").first.click(timeout=3000)
            except:
                break
    else:
        sub_page.get_by_text("资源库编号").locator("//div[@class='x3nfvp2 x120ccyz x1heor9g x1i64zmx']").click()
    sleep(1)


def single_step_sub(page, first):
    try:
        first.get_by_text("查看广告详情").click(timeout=3000)
        process_details(page, True)
    except:
        try:
            first.get_by_text("查看摘要详情").click(timeout=3000)
            process_stack(page)
        except:
            pass

def extract_u_parameter(url):
    # 正则匹配 u= 后面的 URL（%3A%2F%2F 代表 URL 编码的 ://）
    match = re.search(r'[?&]u=([^&]+)', url)

    if match:
        encoded_url = match.group(1)  # 提取匹配的部分
        decoded_url = urllib.parse.unquote(encoded_url)  # 解码 URL
        return decoded_url

    return None  # 如果没有匹配到，返回 None

def get_nearly_month(page):
    while True:
        ads = page.locator(
            "xpath=//div[@class='xrvj5dj xdq2opy xexx8yu xbxaen2 x18d9i69 xbbxn1n xdoe023 xbumo9q x143o31f x7sq92a x1crum5w']").all()
        if len(ads) <= 1:
            page.mouse.wheel(0, delta_y=1000)
        else:
            break
    page.mouse.wheel(0, delta_y=-100000000)
    all = ads[0].locator("xpath=./*").all()
    return all

def filter(url):
    urls_to_filter = [
        'facebook.com', 'youtu.be', 'youtube.com', 't.me', 'wa.me', 'x.com', 'fb.me'
        'privacy', 'zoom', 'amzn', 'wa.aisensy.com', 'instagram', 'tiktok', 'telegram.me', 'python', 'google', 'maps',
        'telegram.dog', 'orcid.org', 'doi.org', 'learn', 'api.whatsapp.com', 'fb.com', 'medium.com', 'channel', 'form',
        'book', 'app.', 'forms', 'aws', 'register', 'microsoft', 'azure', 'products'
    ]
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()

    # 检查域名是否包含任意过滤词
    if any(blocked in domain for blocked in urls_to_filter):
        return False  # 过滤掉不允许的链接
    return True  # 允许的链接

def start(tag):
    global single
    single = set()
    with Camoufox(
            headless=True,
            os="windows",
            # webgl_config=("Apple", "Apple M1, or similar"),
            # os="macos",
            block_webrtc=True,
            window=(1920, 1080),
            locale="zh-CN"
    ) as browser:
        tag = tag.replace(" ", "%20")
        context = browser.new_context()
        page = context.new_page()
        page.goto(
            f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country={country}&is_targeted_country=false&media_type=all&q={tag}&search_type=keyword_unordered",
            timeout=60000)

        ad = get_nearly_month(page)

        for e in ad:
            single_step_sub(page, e)

def fetch_next_task():
    url = f"http://{BASE_URL}/TzsHsAFiR6cbH5EwSt2008X4Jt/next_task"  # 替换为实际 API 地址
    try:
        response = httpx.get(url, timeout=5)
        response.raise_for_status()  # 如果状态码不是 2xx，会抛出异常
        data = response.json()
        return data
    except httpx.RequestError as e:
        return {"status": "error", "message": f"请求失败: {e}"}
    except httpx.HTTPStatusError as e:
        return {"status": "error", "message": f"HTTP 错误: {e.response.status_code}"}
    except ValueError:
        return {"status": "error", "message": "返回数据解析失败"}

def set_country(st):
    global country
    if st == "美国":
        country = "US"
    elif st == "英国":
        country = "GB"
    elif st == "德国":
        country = "DE"
    elif st == "法国":
        country = "FR"
    elif st == "意大利":
        country = "IT"
    elif st == "土耳其":
        country = "TR"
    elif st == "沙特阿拉伯":
        country = "SA"
    elif st == "以色列":
        country = "IL"

if __name__ == '__main__':
    set_country("美国")
    start("ai robot")
    # while True:
    #     task = fetch_next_task()
    #     if task["status"] == "success":
    #         set_country(task["task"]["country"])
    #         start(task["task"]["keyword"])
    #     else:
    #         print(task["message"])
    #         sleep(10)
