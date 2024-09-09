from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore, Style

init(autoreset=True)


def init_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def wait_for_login(driver):
    print(
        Fore.GREEN + "Please log in to 'https://ops.miswag.co/' manually, then press Enter to continue..." + Style.RESET_ALL,
        end='')
    input()


def open_hourly_timeline(driver):
    driver.get("https://ops.miswag.co/timeline/hourly-timeline")


def get_total_orders(driver):
    total_orders_xpath = "/html/body/div[2]/div[2]/main/div/section/header/div/h1"
    total_orders_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, total_orders_xpath)))
    total_orders_text = total_orders_element.text
    total_orders = int(total_orders_text.split()[-1])
    return total_orders


def collect_order_data(driver):
    orders_data = []
    block_index = 23
    while True:
        try:
            title_xpath = f"//*[@id='item-{block_index}']/ol/li/div/div[1]/div"
            title_element = driver.find_element(By.XPATH, title_xpath)
            title = title_element.text
            time_range = title.split(" - ")[1].split(":")[0]
            if time_range == "05" and "PM" in title:
                break
            dispatch_count_xpath = f"//*[@id='item-{block_index}']/ol/li/div/div[2]/ol/li[11]/a/div/div[2]"
            dispatch_count_element = driver.find_element(By.XPATH, dispatch_count_xpath)
            dispatch_count = int(dispatch_count_element.text)
            orders_data.append({
                "time_block": title,
                "dispatch_count": dispatch_count
            })
            block_index -= 1
        except Exception as e:
            print(f"Error occurred while collecting data: {e}")
            break
    return orders_data


def main():
    driver = init_driver()
    driver.get("https://ops.miswag.co/")
    wait_for_login(driver)
    open_hourly_timeline(driver)
    while True:
        print(
            Fore.GREEN + "\nPlease set the desired settings on the timeline page, then press Enter to continue..." + Style.RESET_ALL,
            end='')
        input()
        total_orders = get_total_orders(driver)
        order_data = collect_order_data(driver)
        print(Fore.GREEN + "\nCollected Order Data:" + Style.RESET_ALL, end='')
        print(Fore.RED + f"\nTotal all day {total_orders}" + Style.RESET_ALL, end='')
        total_dispatch_orders = sum(data['dispatch_count'] for data in order_data)
        print(
            Fore.RED + f"\nTotal Dispatch Orders from Last Block till 4 to 5 PM: {total_dispatch_orders}" + Style.RESET_ALL,
            end='')
        print(Fore.YELLOW + "\nPerforming a new check... if done close the app" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
