# !python3
# -*- coding: utf-8 -*-

import time

from pyecharts import options as opts
from pyecharts.charts import Bar, Radar
from pyecharts.render import make_snapshot

from snapshot_selenium import snapshot
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def bar_chart() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c


def draw_radar_for_observation_result() -> Radar:
    value = [[43, 58, 78, 65, 86, 63]]
    min_val = 0
    max_val = 100

    # 用于调整雷达各维度的范围大小
    c_schema = [{"name": "交往能力", "max": max_val, "min": min_val, },
                {"name": "感知能力", "max": max_val, "min": min_val, "color": "#ff0000"},
                {"name": "运动能力", "max": max_val, "min": min_val, "color": "#000000"},
                {"name": "注意力", "max": max_val, "min": min_val, "color": "#00ffff"},
                {"name": "语言能力", "max": max_val, "min": min_val, "color": "#ff00ff"},
                {"name": "自我照顾能力", "max": max_val, "min": min_val, "color": "#ff00ff"}
                ]

    # 画图
    radar = Radar(init_opts=opts.InitOpts(width="750px", height="500px"))
    # radar = Radar()
    radar.add_schema(c_schema, textstyle_opts=opts.TextStyleOpts(color="#3344ff"))
    radar.add(None, value, color="#f9713c",
              symbol='circle', label_opts=opts.LabelOpts(is_show=True),
              areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="#f9713c"))
    # radar.set_global_opts(title_opts=opts.TitleOpts(title="Radar-基本示例"))

    # radar.render("observation_result.html")
    return radar


if __name__ == "__main__":
    start_time = time.time()

    chrome_drive = "chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    browser = webdriver.Chrome(executable_path=chrome_drive, chrome_options=chrome_options)

    # time.sleep(5)

    # make_snapshot(snapshot, bar_chart().render(), "bar0.png")
    make_snapshot(snapshot, draw_radar_for_observation_result().render(), "use_radar.png", is_remove_html=True)

    end_time = time.time()
    print(end_time-start_time)
    browser.close()
