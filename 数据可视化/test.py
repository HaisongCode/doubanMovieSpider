
from pyecharts import Bar
bar = Bar("我的第一个图")
bar.add("服装",["衬衫","羊毛衫","雪芳山","裤子","高跟鞋","袜子"],[5,20,36,10,75,90],is_more_utils=True)
bar.show_config()
bar.render()