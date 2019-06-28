# !python3
# -*- coding: utf-8 -*-

from docx.shared import Mm
from docxtpl import DocxTemplate, RichText, InlineImage

NORMAL_COLOR = "0070c0"
ABNORMAL_COLOR = "#c70000"


def change_docx_template(file_name, new_file_name, template_dict):
    # print(file_name, new_file_name, template_dict)
    docx_file = DocxTemplate(file_name)
    template_dict["rander_image"] = InlineImage(docx_file, template_dict["rander_image"], width=Mm(150))
    docx_file.render(template_dict)
    docx_file.save(new_file_name)


def get_scores_for_table(scores):
    scores_for_table = {}

    for (key, value) in scores.items():
        if value[0] >= 60:
            color = NORMAL_COLOR
        else:
            color = ABNORMAL_COLOR

        value_tmp = []
        for v in value:
            value_tmp.append(RichText(v, color=color))

        scores_for_table[key] = value_tmp

    return scores_for_table


def get_scores_for_para(scores):
    scores_for_para = {}

    for (key, value) in scores.items():
        if value[0] >= 60:
            color = NORMAL_COLOR
        else:
            color = ABNORMAL_COLOR

        value_tmp = [
            RichText(" {} ".format(value[0]), color=color, underline=True),
            RichText(" {} ".format(value[2]), color=color, underline=True)
        ]

        scores_for_para[key] = value_tmp

    return scores_for_para


if __name__ == "__main__":
    observation_scores = {
        "sports_score": [78, '正常', '良好', ''],
        "language_score": [86, '正常', '优秀', ''],
        "communicative_score": [43, '不正常', '不正常', ''],
        "sensory_score": [58, '不正常', '不正常', ''],
        "self_care_score": [63, '正常', '一般', ''],
        "attention_score": [65, '正常', '一般', '']
    }

    template_docx_name = "儿童行为观察系统报告模板.docx"
    new_docx_name = "儿童行为观察系统报告模板_after_2.docx"
    template_dict = {
        "child_name": "{:^5}".format("吴宇"),
        "child_sex": "男",
        "child_age": "{:^2}".format(3),
        "observation_date": "2019/06/14",
        "scores_for_table": get_scores_for_table(observation_scores),
        "scores_for_para": get_scores_for_para(observation_scores),
        "excellent_ability": "语言能力",
        "good_ability": "运动能力",
        "general_ability": "自我照顾能力",
        "abnormal_ability": "交往能力、感知能力",
        "test_table_data": RichText("强化训练(替换后)", color="#0088ff"),
        "rander_image": '../TestPyEcharts/use_radar.png'
    }

    # template_dict = {
    #     "child_name": RichText("吴宇", color="#778899", underline=True, size=28),
    #     "observation_date": "2019/06/14",
    #     "test_table_data": RichText("hello world", font="Arial", color="#0088ff"),
    #     "test_para_data": "非常优秀(替换后)",
    # }

    # template_docx_name = "test.docx"
    # new_docx_name = "test_after.docx"
    # template_dict = {
    #     'template': '123'
    # }

    try:
        change_docx_template(template_docx_name, new_docx_name, template_dict)
    except Exception as e:
        print(e)

    # print(get_scores_for_table(observation_scores))
    # print(get_scores_for_para(observation_scores))

