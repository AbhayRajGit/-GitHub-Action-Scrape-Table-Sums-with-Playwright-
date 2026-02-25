import re
from playwright.sync_api import sync_playwright

def get_seed_sum(page, seed):
    url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
    page.goto(url)
    page.wait_for_selector("table")

    total = 0
    cells = page.locator("table td").all()

    for cell in cells:
        numbers = re.findall(r"-?\d+\.?\d*", cell.inner_text())
        for num in numbers:
            total += float(num)

    print(f"Seed {seed} sum = {total}")
    return total


def main():
    grand_total = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for seed in range(5, 15):
            grand_total += get_seed_sum(page, seed)

        browser.close()

    print("===================================")
    print(f"FINAL TOTAL SUM = {grand_total}")
    print("===================================")


if __name__ == "__main__":
    main()
