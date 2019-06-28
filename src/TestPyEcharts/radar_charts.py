# ! /usr/bin/python3
# -*- coding: utf-8 -*-

from pyecharts.charts import Radar
from pyecharts import options as opts


def draw_radar_for_observation_result():
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
    radar = Radar()
    radar.add_schema(c_schema, textstyle_opts=opts.TextStyleOpts(color="#3344ff"))
    radar.add(None, value, color="#f9713c",
              symbol='circle', label_opts=opts.LabelOpts(is_show=True),
              areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="#f9713c"))
    radar.set_global_opts(title_opts=opts.TitleOpts(title="Radar-基本示例"))

    radar.render("observation_result.html")


if __name__ == "__main__":
    draw_radar_for_observation_result()
