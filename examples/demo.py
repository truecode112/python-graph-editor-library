import pyyed

g = pyyed.Graph()

g.add_node('foo', font_family="Zapfino")
g.add_node('foo2', shape="roundrectangle", font_style="bolditalic",
           underlined_text="true")

g.add_edge('foo1', 'foo2')
g.add_node('abc', font_size="72", height="100")

g.add_node('bar', label="Multi\nline\ntext")
g.add_node('foobar', label="""Multi
Line
Text!""")

g.add_edge('foo', 'foo1', label="EDGE!", width="3.0", color="#0000FF",
           arrowhead="white_diamond", arrowfoot="standard", line_type="dotted")

print(g.get_graph())

print("\n\n\n")

g = pyyed.Graph()
g.add_node('foo', font_family="Zapfino")

gg = g.add_group("MY_Group", shape="diamond")
gg.add_node('foo2', shape="roundrectangle", font_style="bolditalic",
            underlined_text="true")
gg.add_node('abc', font_size="72", height="100")

g.add_edge('foo2', 'abc')
g.add_edge('foo', 'MY_Group')

print(g.get_graph())
