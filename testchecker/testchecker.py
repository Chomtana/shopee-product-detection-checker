import pandas as pd

TOTAL_LEN = 12186

cate_meta = {
  0: "full dress formal",
  1: "full dress",
  2: "tshirt",
  3: "hood",
  4: "yene skirt [color]",
  5: "ring",
  6: "necklace",
  7: "cap",
  8: "wallet",
  9: "bag",
  10: "mobile (android)",
  11: "mobile (iphone)",
  12: "clock",
  13: "bottle dood dai",
  14: "pot",
  15: "coffee [color]",
  16: "shoe",
  17: "shoe song soong",
  18: "air",
  19: "flash drive",
  20: "chair",
  21: "badminton",
  22: "motorcyte cap",
  23: "glove",
  24: "watch",
  25: "belt",
  26: "mini headphone",
  27: "car (toy) [yolo]",
  28: "men jacket",
  29: "men pant",
  30: "shoe pa bai",
  31: "snack",
  32: "mask",
  33: "gel detol [color]",
  34: "cream",
  35: "liquid beauty",
  36: "wares",
  37: "notebook",
  38: "bucket",
  39: "vase",
  40: "fukbua",
  41: "sofa",
}

cates = {}

summary_list = ""

df = pd.read_csv("submission.csv")

for row in df.itertuples():
  if row.category in cates:
    cates[row.category].append(row.filename)
  else:
    cates[row.category] = [row.filename]

for cate in cates.items():
  bodyview = ""

  for pic in cate[1]:
    bodyview += '<img class="item" src="../test/test/'+pic+'">\n'

  style = """
        <style>
          .item {
            flex-basis: 128px;
            width: 128px;
            height: 128px;
            margin: 4px;
          }
        </style>
  """

  res = """
    <!doctype html>
    <html>
      <head>
        {style}
      </head>
      <body>
        <h2>{cateid} - {catename}</h2>
        <h3>Count: {catelen} {catepercent}/{catepercentbase}</h3>
        <div style="display: flex; flex-wrap: wrap;">
          {bodyview}
        </div>
      </body>
    </html>
  """.format(
    cateid=cate[0],
    catename=cate_meta[cate[0]],
    catelen=str(len(cate[1])),
    catepercent="%.4f" % (len(cate[1]) / TOTAL_LEN),
    catepercentbase="%.4f" % (1 / 42),
    bodyview = bodyview,
    style = style,
  )

  summary_list += '<li><a href="./{cateid}_{catename}.html">{cateid} - {catename} [ {catelen} {catepercent}/{catepercentbase} ]</a></li>\n'.format(
    cateid=cate[0],
    catename=cate_meta[cate[0]],
    catelen=str(len(cate[1])),
    catepercent="%.4f" % (len(cate[1]) / TOTAL_LEN),
    catepercentbase="%.4f" % (1 / 42),
  )

  file = open(str(cate[0])+'_'+cate_meta[cate[0]]+'.html', 'w', encoding='utf-8')
  file.write(res)

summary = """
  <!doctype html>
  <html>
    <head>
      <title>Summary</title>
    </head>
    <body>
      <h2>Summary</h2>
      <ul>
        {summary_list}
      </ul>
    </body>
  </html>
""".format(summary_list = summary_list)

open("index.html", "w", encoding="utf-8").write(summary)