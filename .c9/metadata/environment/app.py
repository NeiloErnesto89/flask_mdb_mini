{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":60,"column":15},"end":{"row":60,"column":17},"action":"insert","lines":["()"],"id":369}],[{"start":{"row":60,"column":16},"end":{"row":60,"column":17},"action":"insert","lines":["t"],"id":370},{"start":{"row":60,"column":17},"end":{"row":60,"column":18},"action":"insert","lines":["a"]},{"start":{"row":60,"column":18},"end":{"row":60,"column":19},"action":"insert","lines":["s"]},{"start":{"row":60,"column":19},"end":{"row":60,"column":20},"action":"insert","lines":["k"]}],[{"start":{"row":60,"column":16},"end":{"row":60,"column":20},"action":"remove","lines":["task"],"id":371},{"start":{"row":60,"column":16},"end":{"row":60,"column":23},"action":"insert","lines":["task_id"]}],[{"start":{"row":60,"column":24},"end":{"row":60,"column":25},"action":"insert","lines":[":"],"id":372}],[{"start":{"row":60,"column":25},"end":{"row":61,"column":0},"action":"insert","lines":["",""],"id":373},{"start":{"row":61,"column":0},"end":{"row":61,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":61,"column":4},"end":{"row":61,"column":5},"action":"insert","lines":["m"],"id":374},{"start":{"row":61,"column":5},"end":{"row":61,"column":6},"action":"insert","lines":["o"]},{"start":{"row":61,"column":6},"end":{"row":61,"column":7},"action":"insert","lines":["n"]},{"start":{"row":61,"column":7},"end":{"row":61,"column":8},"action":"insert","lines":["g"]},{"start":{"row":61,"column":8},"end":{"row":61,"column":9},"action":"insert","lines":["o"]},{"start":{"row":61,"column":9},"end":{"row":61,"column":10},"action":"insert","lines":["."]},{"start":{"row":61,"column":10},"end":{"row":61,"column":11},"action":"insert","lines":["d"]},{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"remove","lines":["e"],"id":375}],[{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"insert","lines":["b"],"id":376},{"start":{"row":61,"column":12},"end":{"row":61,"column":13},"action":"insert","lines":["."]}],[{"start":{"row":61,"column":13},"end":{"row":61,"column":14},"action":"insert","lines":["t"],"id":377},{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"insert","lines":["a"]},{"start":{"row":61,"column":15},"end":{"row":61,"column":16},"action":"insert","lines":["s"]},{"start":{"row":61,"column":16},"end":{"row":61,"column":17},"action":"insert","lines":["k"]},{"start":{"row":61,"column":17},"end":{"row":61,"column":18},"action":"insert","lines":["s"]},{"start":{"row":61,"column":18},"end":{"row":61,"column":19},"action":"insert","lines":["."]},{"start":{"row":61,"column":19},"end":{"row":61,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":61,"column":20},"end":{"row":61,"column":21},"action":"insert","lines":["e"],"id":378},{"start":{"row":61,"column":21},"end":{"row":61,"column":22},"action":"insert","lines":["m"]},{"start":{"row":61,"column":22},"end":{"row":61,"column":23},"action":"insert","lines":["o"]},{"start":{"row":61,"column":23},"end":{"row":61,"column":24},"action":"insert","lines":["v"]},{"start":{"row":61,"column":24},"end":{"row":61,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":61,"column":25},"end":{"row":61,"column":27},"action":"insert","lines":["()"],"id":379}],[{"start":{"row":61,"column":27},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":380},{"start":{"row":62,"column":0},"end":{"row":62,"column":4},"action":"insert","lines":["    "]},{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"insert","lines":[" "]}],[{"start":{"row":62,"column":5},"end":{"row":62,"column":43},"action":"insert","lines":[" return redirect(url_for('get_tasks'))"],"id":381}],[{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"remove","lines":[" "],"id":382},{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":61,"column":26},"end":{"row":61,"column":52},"action":"insert","lines":["{\"_id\": ObjectId(task_id)}"],"id":383}],[{"start":{"row":59,"column":0},"end":{"row":60,"column":0},"action":"insert","lines":["",""],"id":384}],[{"start":{"row":60,"column":0},"end":{"row":63,"column":41},"action":"remove","lines":["@app.route('/delete_task/<task_id>')","def delete_task(task_id):","    mongo.db.tasks.remove({\"_id\": ObjectId(task_id)})","    return redirect(url_for('get_tasks'))"],"id":385},{"start":{"row":60,"column":0},"end":{"row":63,"column":41},"action":"insert","lines":["@app.route('/delete_task/<task_id>')","def delete_task(task_id):","    mongo.db.tasks.remove({'_id': ObjectId(task_id)})","    return redirect(url_for('get_tasks'))"]}],[{"start":{"row":63,"column":41},"end":{"row":64,"column":0},"action":"insert","lines":["",""],"id":386},{"start":{"row":64,"column":0},"end":{"row":64,"column":4},"action":"insert","lines":["    "]},{"start":{"row":64,"column":4},"end":{"row":65,"column":0},"action":"insert","lines":["",""]},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"remove","lines":["    "],"id":387},{"start":{"row":64,"column":4},"end":{"row":65,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":64,"column":4},"end":{"row":65,"column":0},"action":"insert","lines":["",""],"id":388},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"remove","lines":["    "],"id":389}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":1},"action":"insert","lines":["@"],"id":390},{"start":{"row":65,"column":1},"end":{"row":65,"column":2},"action":"insert","lines":["a"]},{"start":{"row":65,"column":2},"end":{"row":65,"column":3},"action":"insert","lines":["p"]},{"start":{"row":65,"column":3},"end":{"row":65,"column":4},"action":"insert","lines":["p"]},{"start":{"row":65,"column":4},"end":{"row":65,"column":5},"action":"insert","lines":["."]},{"start":{"row":65,"column":5},"end":{"row":65,"column":6},"action":"insert","lines":["r"]},{"start":{"row":65,"column":6},"end":{"row":65,"column":7},"action":"insert","lines":["o"]},{"start":{"row":65,"column":7},"end":{"row":65,"column":8},"action":"insert","lines":["u"]},{"start":{"row":65,"column":8},"end":{"row":65,"column":9},"action":"insert","lines":["t"]},{"start":{"row":65,"column":9},"end":{"row":65,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":65,"column":10},"end":{"row":65,"column":12},"action":"insert","lines":["()"],"id":391}],[{"start":{"row":65,"column":11},"end":{"row":65,"column":13},"action":"insert","lines":["''"],"id":392}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":14},"action":"remove","lines":["@app.route('')"],"id":393},{"start":{"row":65,"column":0},"end":{"row":68,"column":65},"action":"insert","lines":["@app.route('/get_categories')","def get_categories():","    return render_template('categories.html',","                           categories=mongo.db.categories.find())"]}],[{"start":{"row":68,"column":65},"end":{"row":69,"column":0},"action":"insert","lines":["",""],"id":394},{"start":{"row":69,"column":0},"end":{"row":69,"column":27},"action":"insert","lines":["                           "]},{"start":{"row":69,"column":27},"end":{"row":70,"column":0},"action":"insert","lines":["",""]},{"start":{"row":70,"column":0},"end":{"row":70,"column":27},"action":"insert","lines":["                           "]}],[{"start":{"row":70,"column":26},"end":{"row":70,"column":27},"action":"remove","lines":[" "],"id":395},{"start":{"row":70,"column":25},"end":{"row":70,"column":26},"action":"remove","lines":[" "]},{"start":{"row":70,"column":24},"end":{"row":70,"column":25},"action":"remove","lines":[" "]},{"start":{"row":70,"column":20},"end":{"row":70,"column":24},"action":"remove","lines":["    "]},{"start":{"row":70,"column":16},"end":{"row":70,"column":20},"action":"remove","lines":["    "]},{"start":{"row":70,"column":12},"end":{"row":70,"column":16},"action":"remove","lines":["    "]},{"start":{"row":70,"column":8},"end":{"row":70,"column":12},"action":"remove","lines":["    "]},{"start":{"row":70,"column":4},"end":{"row":70,"column":8},"action":"remove","lines":["    "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":70,"column":0},"end":{"row":70,"column":29},"action":"insert","lines":["@app.route('/get_categories')"],"id":396}],[{"start":{"row":70,"column":13},"end":{"row":70,"column":27},"action":"remove","lines":["get_categories"],"id":397},{"start":{"row":70,"column":13},"end":{"row":70,"column":14},"action":"insert","lines":["E"]},{"start":{"row":70,"column":14},"end":{"row":70,"column":15},"action":"insert","lines":["D"]},{"start":{"row":70,"column":15},"end":{"row":70,"column":16},"action":"insert","lines":["I"]},{"start":{"row":70,"column":16},"end":{"row":70,"column":17},"action":"insert","lines":["T"]}],[{"start":{"row":70,"column":16},"end":{"row":70,"column":17},"action":"remove","lines":["T"],"id":398},{"start":{"row":70,"column":15},"end":{"row":70,"column":16},"action":"remove","lines":["I"]},{"start":{"row":70,"column":14},"end":{"row":70,"column":15},"action":"remove","lines":["D"]},{"start":{"row":70,"column":13},"end":{"row":70,"column":14},"action":"remove","lines":["E"]}],[{"start":{"row":70,"column":13},"end":{"row":70,"column":14},"action":"insert","lines":["e"],"id":399},{"start":{"row":70,"column":14},"end":{"row":70,"column":15},"action":"insert","lines":["d"]},{"start":{"row":70,"column":15},"end":{"row":70,"column":16},"action":"insert","lines":["i"]},{"start":{"row":70,"column":16},"end":{"row":70,"column":17},"action":"insert","lines":["t"]},{"start":{"row":70,"column":17},"end":{"row":70,"column":18},"action":"insert","lines":["_"]},{"start":{"row":70,"column":18},"end":{"row":70,"column":19},"action":"insert","lines":["c"]}],[{"start":{"row":70,"column":19},"end":{"row":70,"column":20},"action":"insert","lines":["a"],"id":400}],[{"start":{"row":70,"column":13},"end":{"row":70,"column":20},"action":"remove","lines":["edit_ca"],"id":401},{"start":{"row":70,"column":13},"end":{"row":70,"column":26},"action":"insert","lines":["edit_category"]}],[{"start":{"row":70,"column":27},"end":{"row":70,"column":28},"action":"insert","lines":["/"],"id":402},{"start":{"row":70,"column":28},"end":{"row":70,"column":29},"action":"insert","lines":["<"]},{"start":{"row":70,"column":29},"end":{"row":70,"column":30},"action":"insert","lines":["c"]}],[{"start":{"row":70,"column":30},"end":{"row":70,"column":31},"action":"insert","lines":["a"],"id":403},{"start":{"row":70,"column":31},"end":{"row":70,"column":32},"action":"insert","lines":["t"]},{"start":{"row":70,"column":32},"end":{"row":70,"column":33},"action":"insert","lines":["e"]}],[{"start":{"row":70,"column":29},"end":{"row":70,"column":33},"action":"remove","lines":["cate"],"id":404},{"start":{"row":70,"column":29},"end":{"row":70,"column":40},"action":"insert","lines":["category_id"]}],[{"start":{"row":70,"column":40},"end":{"row":70,"column":41},"action":"insert","lines":[">"],"id":405}],[{"start":{"row":70,"column":41},"end":{"row":70,"column":43},"action":"insert","lines":["''"],"id":406}],[{"start":{"row":70,"column":26},"end":{"row":70,"column":27},"action":"remove","lines":["'"],"id":407}],[{"start":{"row":70,"column":41},"end":{"row":70,"column":42},"action":"remove","lines":["'"],"id":408}],[{"start":{"row":70,"column":42},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":409},{"start":{"row":71,"column":0},"end":{"row":71,"column":1},"action":"insert","lines":["d"]},{"start":{"row":71,"column":1},"end":{"row":71,"column":2},"action":"insert","lines":["e"]},{"start":{"row":71,"column":2},"end":{"row":71,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":71,"column":3},"end":{"row":71,"column":4},"action":"insert","lines":[" "],"id":410},{"start":{"row":71,"column":4},"end":{"row":71,"column":5},"action":"insert","lines":["e"]},{"start":{"row":71,"column":5},"end":{"row":71,"column":6},"action":"insert","lines":["d"]},{"start":{"row":71,"column":6},"end":{"row":71,"column":7},"action":"insert","lines":["i"]},{"start":{"row":71,"column":7},"end":{"row":71,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":71,"column":4},"end":{"row":71,"column":8},"action":"remove","lines":["edit"],"id":411},{"start":{"row":71,"column":4},"end":{"row":71,"column":17},"action":"insert","lines":["edit_category"]}],[{"start":{"row":71,"column":17},"end":{"row":71,"column":19},"action":"insert","lines":["()"],"id":412}],[{"start":{"row":71,"column":18},"end":{"row":71,"column":19},"action":"insert","lines":["c"],"id":413},{"start":{"row":71,"column":19},"end":{"row":71,"column":20},"action":"insert","lines":["a"]},{"start":{"row":71,"column":20},"end":{"row":71,"column":21},"action":"insert","lines":["t"]},{"start":{"row":71,"column":21},"end":{"row":71,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":71,"column":18},"end":{"row":71,"column":22},"action":"remove","lines":["cate"],"id":414},{"start":{"row":71,"column":18},"end":{"row":71,"column":29},"action":"insert","lines":["category_id"]}],[{"start":{"row":71,"column":30},"end":{"row":71,"column":31},"action":"insert","lines":[":"],"id":415}],[{"start":{"row":71,"column":31},"end":{"row":72,"column":0},"action":"insert","lines":["",""],"id":416},{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":72,"column":4},"end":{"row":72,"column":5},"action":"insert","lines":["r"],"id":417},{"start":{"row":72,"column":5},"end":{"row":72,"column":6},"action":"insert","lines":["e"]},{"start":{"row":72,"column":6},"end":{"row":72,"column":7},"action":"insert","lines":["t"]},{"start":{"row":72,"column":7},"end":{"row":72,"column":8},"action":"insert","lines":["u"]},{"start":{"row":72,"column":8},"end":{"row":72,"column":9},"action":"insert","lines":["r"]}],[{"start":{"row":72,"column":9},"end":{"row":72,"column":10},"action":"insert","lines":["n"],"id":418}],[{"start":{"row":72,"column":10},"end":{"row":72,"column":11},"action":"insert","lines":[" "],"id":419},{"start":{"row":72,"column":11},"end":{"row":72,"column":12},"action":"insert","lines":["r"]},{"start":{"row":72,"column":12},"end":{"row":72,"column":13},"action":"insert","lines":["e"]},{"start":{"row":72,"column":13},"end":{"row":72,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":72,"column":11},"end":{"row":72,"column":14},"action":"remove","lines":["ren"],"id":420},{"start":{"row":72,"column":11},"end":{"row":72,"column":26},"action":"insert","lines":["render_template"]}],[{"start":{"row":72,"column":26},"end":{"row":72,"column":28},"action":"insert","lines":["()"],"id":421}],[{"start":{"row":72,"column":27},"end":{"row":72,"column":29},"action":"insert","lines":["''"],"id":422}],[{"start":{"row":72,"column":28},"end":{"row":72,"column":29},"action":"insert","lines":["e"],"id":423},{"start":{"row":72,"column":29},"end":{"row":72,"column":30},"action":"insert","lines":["d"]},{"start":{"row":72,"column":30},"end":{"row":72,"column":31},"action":"insert","lines":["i"]}],[{"start":{"row":72,"column":31},"end":{"row":72,"column":32},"action":"insert","lines":["t"],"id":424},{"start":{"row":72,"column":32},"end":{"row":72,"column":33},"action":"insert","lines":["c"]},{"start":{"row":72,"column":33},"end":{"row":72,"column":34},"action":"insert","lines":["a"]},{"start":{"row":72,"column":34},"end":{"row":72,"column":35},"action":"insert","lines":["t"]},{"start":{"row":72,"column":35},"end":{"row":72,"column":36},"action":"insert","lines":["e"]},{"start":{"row":72,"column":36},"end":{"row":72,"column":37},"action":"insert","lines":["g"]},{"start":{"row":72,"column":37},"end":{"row":72,"column":38},"action":"insert","lines":["o"]},{"start":{"row":72,"column":38},"end":{"row":72,"column":39},"action":"insert","lines":["r"]},{"start":{"row":72,"column":39},"end":{"row":72,"column":40},"action":"insert","lines":["y"]},{"start":{"row":72,"column":40},"end":{"row":72,"column":41},"action":"insert","lines":["."]},{"start":{"row":72,"column":41},"end":{"row":72,"column":42},"action":"insert","lines":["h"]},{"start":{"row":72,"column":42},"end":{"row":72,"column":43},"action":"insert","lines":["t"]},{"start":{"row":72,"column":43},"end":{"row":72,"column":44},"action":"insert","lines":["m"]}],[{"start":{"row":72,"column":44},"end":{"row":72,"column":45},"action":"insert","lines":["l"],"id":425}],[{"start":{"row":72,"column":46},"end":{"row":72,"column":47},"action":"insert","lines":[","],"id":426}],[{"start":{"row":72,"column":47},"end":{"row":72,"column":48},"action":"insert","lines":[" "],"id":427}],[{"start":{"row":72,"column":48},"end":{"row":72,"column":49},"action":"insert","lines":["c"],"id":428},{"start":{"row":72,"column":49},"end":{"row":72,"column":50},"action":"insert","lines":["a"]},{"start":{"row":72,"column":50},"end":{"row":72,"column":51},"action":"insert","lines":["t"]},{"start":{"row":72,"column":51},"end":{"row":72,"column":52},"action":"insert","lines":["e"]},{"start":{"row":72,"column":52},"end":{"row":72,"column":53},"action":"insert","lines":["g"]},{"start":{"row":72,"column":53},"end":{"row":72,"column":54},"action":"insert","lines":["o"]},{"start":{"row":72,"column":54},"end":{"row":72,"column":55},"action":"insert","lines":["r"]}],[{"start":{"row":72,"column":55},"end":{"row":72,"column":56},"action":"insert","lines":["y"],"id":429},{"start":{"row":72,"column":56},"end":{"row":72,"column":57},"action":"insert","lines":["="]},{"start":{"row":72,"column":57},"end":{"row":72,"column":58},"action":"insert","lines":["m"]},{"start":{"row":72,"column":58},"end":{"row":72,"column":59},"action":"insert","lines":["o"]},{"start":{"row":72,"column":59},"end":{"row":72,"column":60},"action":"insert","lines":["n"]},{"start":{"row":72,"column":60},"end":{"row":72,"column":61},"action":"insert","lines":["g"]},{"start":{"row":72,"column":61},"end":{"row":72,"column":62},"action":"insert","lines":["o"]}],[{"start":{"row":72,"column":62},"end":{"row":72,"column":63},"action":"insert","lines":["."],"id":430},{"start":{"row":72,"column":63},"end":{"row":72,"column":64},"action":"insert","lines":["d"]},{"start":{"row":72,"column":64},"end":{"row":72,"column":65},"action":"insert","lines":["b"]},{"start":{"row":72,"column":65},"end":{"row":72,"column":66},"action":"insert","lines":["."]},{"start":{"row":72,"column":66},"end":{"row":72,"column":67},"action":"insert","lines":["c"]}],[{"start":{"row":72,"column":67},"end":{"row":72,"column":68},"action":"insert","lines":["a"],"id":431},{"start":{"row":72,"column":68},"end":{"row":72,"column":69},"action":"insert","lines":["t"]},{"start":{"row":72,"column":69},"end":{"row":72,"column":70},"action":"insert","lines":["e"]},{"start":{"row":72,"column":70},"end":{"row":72,"column":71},"action":"insert","lines":["g"]}],[{"start":{"row":72,"column":66},"end":{"row":72,"column":71},"action":"remove","lines":["categ"],"id":432},{"start":{"row":72,"column":66},"end":{"row":72,"column":76},"action":"insert","lines":["categories"]}],[{"start":{"row":72,"column":76},"end":{"row":72,"column":77},"action":"insert","lines":["."],"id":433},{"start":{"row":72,"column":77},"end":{"row":72,"column":78},"action":"insert","lines":["f"]},{"start":{"row":72,"column":78},"end":{"row":72,"column":79},"action":"insert","lines":["i"]},{"start":{"row":72,"column":79},"end":{"row":72,"column":80},"action":"insert","lines":["n"]},{"start":{"row":72,"column":80},"end":{"row":72,"column":81},"action":"insert","lines":["d"]}],[{"start":{"row":72,"column":77},"end":{"row":72,"column":81},"action":"remove","lines":["find"],"id":434},{"start":{"row":72,"column":77},"end":{"row":72,"column":85},"action":"insert","lines":["find_one"]}],[{"start":{"row":72,"column":85},"end":{"row":72,"column":87},"action":"insert","lines":["()"],"id":435}],[{"start":{"row":72,"column":86},"end":{"row":72,"column":88},"action":"insert","lines":["{}"],"id":436}],[{"start":{"row":72,"column":48},"end":{"row":72,"column":90},"action":"remove","lines":["category=mongo.db.categories.find_one({}))"],"id":437},{"start":{"row":72,"column":48},"end":{"row":73,"column":59},"action":"insert","lines":["category=mongo.db.categories.find_one(","                           {'_id': ObjectId(category_id)}))"]}],[{"start":{"row":73,"column":26},"end":{"row":73,"column":27},"action":"remove","lines":[" "],"id":438},{"start":{"row":73,"column":25},"end":{"row":73,"column":26},"action":"remove","lines":[" "]},{"start":{"row":73,"column":24},"end":{"row":73,"column":25},"action":"remove","lines":[" "]},{"start":{"row":73,"column":20},"end":{"row":73,"column":24},"action":"remove","lines":["    "]},{"start":{"row":73,"column":16},"end":{"row":73,"column":20},"action":"remove","lines":["    "]},{"start":{"row":73,"column":12},"end":{"row":73,"column":16},"action":"remove","lines":["    "]},{"start":{"row":73,"column":8},"end":{"row":73,"column":12},"action":"remove","lines":["    "]},{"start":{"row":73,"column":4},"end":{"row":73,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":73,"column":36},"end":{"row":74,"column":0},"action":"insert","lines":["",""],"id":439},{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"insert","lines":["    "]},{"start":{"row":74,"column":4},"end":{"row":75,"column":0},"action":"insert","lines":["",""]},{"start":{"row":75,"column":0},"end":{"row":75,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":75,"column":0},"end":{"row":75,"column":4},"action":"remove","lines":["    "],"id":440}],[{"start":{"row":75,"column":0},"end":{"row":75,"column":1},"action":"insert","lines":["@"],"id":441},{"start":{"row":75,"column":1},"end":{"row":75,"column":2},"action":"insert","lines":["a"]},{"start":{"row":75,"column":2},"end":{"row":75,"column":3},"action":"insert","lines":["p"]},{"start":{"row":75,"column":3},"end":{"row":75,"column":4},"action":"insert","lines":["p"]},{"start":{"row":75,"column":4},"end":{"row":75,"column":5},"action":"insert","lines":["."]},{"start":{"row":75,"column":5},"end":{"row":75,"column":6},"action":"insert","lines":["r"]},{"start":{"row":75,"column":6},"end":{"row":75,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":75,"column":7},"end":{"row":75,"column":8},"action":"insert","lines":["u"],"id":442},{"start":{"row":75,"column":8},"end":{"row":75,"column":9},"action":"insert","lines":["t"]},{"start":{"row":75,"column":9},"end":{"row":75,"column":10},"action":"insert","lines":["e"]},{"start":{"row":75,"column":10},"end":{"row":75,"column":11},"action":"insert","lines":["{"]}],[{"start":{"row":75,"column":10},"end":{"row":75,"column":11},"action":"remove","lines":["{"],"id":443}],[{"start":{"row":75,"column":10},"end":{"row":75,"column":12},"action":"insert","lines":["()"],"id":444}],[{"start":{"row":75,"column":11},"end":{"row":75,"column":13},"action":"insert","lines":["''"],"id":445}],[{"start":{"row":75,"column":12},"end":{"row":75,"column":13},"action":"insert","lines":["/"],"id":446},{"start":{"row":75,"column":13},"end":{"row":75,"column":14},"action":"insert","lines":["u"]},{"start":{"row":75,"column":14},"end":{"row":75,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":75,"column":14},"end":{"row":75,"column":15},"action":"remove","lines":["d"],"id":447}],[{"start":{"row":75,"column":14},"end":{"row":75,"column":15},"action":"insert","lines":["p"],"id":448},{"start":{"row":75,"column":15},"end":{"row":75,"column":16},"action":"insert","lines":["d"]},{"start":{"row":75,"column":16},"end":{"row":75,"column":17},"action":"insert","lines":["a"]},{"start":{"row":75,"column":17},"end":{"row":75,"column":18},"action":"insert","lines":["t"]},{"start":{"row":75,"column":18},"end":{"row":75,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":75,"column":19},"end":{"row":75,"column":20},"action":"insert","lines":["_"],"id":449},{"start":{"row":75,"column":20},"end":{"row":75,"column":21},"action":"insert","lines":["c"]},{"start":{"row":75,"column":21},"end":{"row":75,"column":22},"action":"insert","lines":["a"]},{"start":{"row":75,"column":22},"end":{"row":75,"column":23},"action":"insert","lines":["t"]},{"start":{"row":75,"column":23},"end":{"row":75,"column":24},"action":"insert","lines":["e"]},{"start":{"row":75,"column":24},"end":{"row":75,"column":25},"action":"insert","lines":["g"]},{"start":{"row":75,"column":25},"end":{"row":75,"column":26},"action":"insert","lines":["o"]},{"start":{"row":75,"column":26},"end":{"row":75,"column":27},"action":"insert","lines":["r"]},{"start":{"row":75,"column":27},"end":{"row":75,"column":28},"action":"insert","lines":["y"]}],[{"start":{"row":75,"column":0},"end":{"row":75,"column":1},"action":"remove","lines":["@"],"id":450}],[{"start":{"row":75,"column":0},"end":{"row":75,"column":29},"action":"remove","lines":["app.route('/update_category')"],"id":451},{"start":{"row":74,"column":4},"end":{"row":75,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":70,"column":0},"end":{"row":73,"column":36},"action":"remove","lines":["@app.route('/edit_category/<category_id>')","def edit_category(category_id):","    return render_template('editcategory.html', category=mongo.db.categories.find_one(","    {'_id': ObjectId(category_id)}))"],"id":452},{"start":{"row":70,"column":0},"end":{"row":74,"column":59},"action":"insert","lines":["@app.route('/edit_category/<category_id>')","def edit_category(category_id):","    return render_template('editcategory.html',","                           category=mongo.db.categories.find_one(","                           {'_id': ObjectId(category_id)}))"]}],[{"start":{"row":74,"column":59},"end":{"row":75,"column":0},"action":"insert","lines":["",""],"id":453},{"start":{"row":75,"column":0},"end":{"row":75,"column":27},"action":"insert","lines":["                           "]},{"start":{"row":75,"column":27},"end":{"row":76,"column":0},"action":"insert","lines":["",""]},{"start":{"row":76,"column":0},"end":{"row":76,"column":27},"action":"insert","lines":["                           "]}],[{"start":{"row":76,"column":26},"end":{"row":76,"column":27},"action":"remove","lines":[" "],"id":454},{"start":{"row":76,"column":25},"end":{"row":76,"column":26},"action":"remove","lines":[" "]},{"start":{"row":76,"column":24},"end":{"row":76,"column":25},"action":"remove","lines":[" "]},{"start":{"row":76,"column":20},"end":{"row":76,"column":24},"action":"remove","lines":["    "]},{"start":{"row":76,"column":16},"end":{"row":76,"column":20},"action":"remove","lines":["    "]},{"start":{"row":76,"column":12},"end":{"row":76,"column":16},"action":"remove","lines":["    "]},{"start":{"row":76,"column":8},"end":{"row":76,"column":12},"action":"remove","lines":["    "]},{"start":{"row":76,"column":4},"end":{"row":76,"column":8},"action":"remove","lines":["    "]},{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":76,"column":0},"end":{"row":81,"column":46},"action":"insert","lines":["@app.route('/update_category/<category_id>', methods=['POST'])","def update_category(category_id):","    mongo.db.categories.update(","        {'_id': ObjectId(category_id)},","        {'category_name': request.form.get('category_name')})","    return redirect(url_for('get_categories'))"],"id":455}],[{"start":{"row":65,"column":0},"end":{"row":82,"column":4},"action":"remove","lines":["@app.route('/get_categories')","def get_categories():","    return render_template('categories.html',","                           categories=mongo.db.categories.find())","                           ","@app.route('/edit_category/<category_id>')","def edit_category(category_id):","    return render_template('editcategory.html',","                           category=mongo.db.categories.find_one(","                           {'_id': ObjectId(category_id)}))","                           ","@app.route('/update_category/<category_id>', methods=['POST'])","def update_category(category_id):","    mongo.db.categories.update(","        {'_id': ObjectId(category_id)},","        {'category_name': request.form.get('category_name')})","    return redirect(url_for('get_categories'))","    "],"id":456},{"start":{"row":65,"column":0},"end":{"row":83,"column":46},"action":"insert","lines":["@app.route('/get_categories')","def get_categories():","    return render_template('categories.html',","                           categories=mongo.db.categories.find())","                           ","","@app.route('/edit_category/<category_id>')","def edit_category(category_id):","    return render_template('editcategory.html',","                           category=mongo.db.categories.find_one(","                           {'_id': ObjectId(category_id)}))","","","@app.route('/update_category/<category_id>', methods=['POST'])","def update_category(category_id):","    mongo.db.categories.update(","        {'_id': ObjectId(category_id)},","        {'category_name': request.form.get('category_name')})","    return redirect(url_for('get_categories'))"]}],[{"start":{"row":83,"column":46},"end":{"row":84,"column":0},"action":"insert","lines":["",""],"id":457},{"start":{"row":84,"column":0},"end":{"row":84,"column":4},"action":"insert","lines":["    "]},{"start":{"row":84,"column":4},"end":{"row":85,"column":0},"action":"insert","lines":["",""]},{"start":{"row":85,"column":0},"end":{"row":85,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":85,"column":0},"end":{"row":85,"column":4},"action":"remove","lines":["    "],"id":458}],[{"start":{"row":85,"column":0},"end":{"row":88,"column":46},"action":"insert","lines":["@app.route('/delete_category/<category_id>')","def delete_category(category_id):","    mongo.db.categories.remove({'_id': ObjectId(category_id)})","    return redirect(url_for('get_categories'))"],"id":459}],[{"start":{"row":88,"column":46},"end":{"row":89,"column":0},"action":"insert","lines":["",""],"id":460},{"start":{"row":89,"column":0},"end":{"row":89,"column":4},"action":"insert","lines":["    "]},{"start":{"row":89,"column":4},"end":{"row":90,"column":0},"action":"insert","lines":["",""]},{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"remove","lines":["    "],"id":461}],[{"start":{"row":90,"column":0},"end":{"row":99,"column":46},"action":"insert","lines":["@app.route('/insert_category', methods=['POST'])","def insert_category():","    category_doc = {'category_name': request.form.get('category_name')}","    mongo.db.categories.insert_one(category_doc)","    return redirect(url_for('get_categories'))","","","@app.route('/add_category')","def add_category():","    return render_template('addcategory.html')"],"id":462}],[{"start":{"row":88,"column":46},"end":{"row":89,"column":0},"action":"insert","lines":["",""],"id":463},{"start":{"row":89,"column":0},"end":{"row":89,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":84,"column":4},"end":{"row":85,"column":0},"action":"insert","lines":["",""],"id":464},{"start":{"row":85,"column":0},"end":{"row":85,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":93,"column":22},"end":{"row":94,"column":0},"action":"insert","lines":["",""],"id":465},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"insert","lines":["    "]},{"start":{"row":94,"column":4},"end":{"row":94,"column":5},"action":"insert","lines":["c"]},{"start":{"row":94,"column":5},"end":{"row":94,"column":6},"action":"insert","lines":["a"]},{"start":{"row":94,"column":6},"end":{"row":94,"column":7},"action":"insert","lines":["t"]},{"start":{"row":94,"column":7},"end":{"row":94,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":94,"column":8},"end":{"row":94,"column":9},"action":"insert","lines":["g"],"id":466},{"start":{"row":94,"column":9},"end":{"row":94,"column":10},"action":"insert","lines":["o"]},{"start":{"row":94,"column":10},"end":{"row":94,"column":11},"action":"insert","lines":["r"]},{"start":{"row":94,"column":11},"end":{"row":94,"column":12},"action":"insert","lines":["i"]},{"start":{"row":94,"column":12},"end":{"row":94,"column":13},"action":"insert","lines":["e"]},{"start":{"row":94,"column":13},"end":{"row":94,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":94,"column":14},"end":{"row":94,"column":15},"action":"insert","lines":[" "],"id":467},{"start":{"row":94,"column":15},"end":{"row":94,"column":16},"action":"insert","lines":["="]}],[{"start":{"row":94,"column":16},"end":{"row":94,"column":17},"action":"insert","lines":[" "],"id":468},{"start":{"row":94,"column":17},"end":{"row":94,"column":18},"action":"insert","lines":["m"]},{"start":{"row":94,"column":18},"end":{"row":94,"column":19},"action":"insert","lines":["o"]},{"start":{"row":94,"column":19},"end":{"row":94,"column":20},"action":"insert","lines":["n"]},{"start":{"row":94,"column":20},"end":{"row":94,"column":21},"action":"insert","lines":["g"]},{"start":{"row":94,"column":21},"end":{"row":94,"column":22},"action":"insert","lines":["o"]},{"start":{"row":94,"column":22},"end":{"row":94,"column":23},"action":"insert","lines":["."]},{"start":{"row":94,"column":23},"end":{"row":94,"column":24},"action":"insert","lines":["d"]},{"start":{"row":94,"column":24},"end":{"row":94,"column":25},"action":"insert","lines":["b"]}],[{"start":{"row":94,"column":25},"end":{"row":94,"column":26},"action":"insert","lines":["."],"id":469},{"start":{"row":94,"column":26},"end":{"row":94,"column":27},"action":"insert","lines":["c"]},{"start":{"row":94,"column":27},"end":{"row":94,"column":28},"action":"insert","lines":["a"]},{"start":{"row":94,"column":28},"end":{"row":94,"column":29},"action":"insert","lines":["t"]},{"start":{"row":94,"column":29},"end":{"row":94,"column":30},"action":"insert","lines":["e"]},{"start":{"row":94,"column":30},"end":{"row":94,"column":31},"action":"insert","lines":["g"]},{"start":{"row":94,"column":31},"end":{"row":94,"column":32},"action":"insert","lines":["o"]},{"start":{"row":94,"column":32},"end":{"row":94,"column":33},"action":"insert","lines":["r"]},{"start":{"row":94,"column":33},"end":{"row":94,"column":34},"action":"insert","lines":["i"]},{"start":{"row":94,"column":34},"end":{"row":94,"column":35},"action":"insert","lines":["e"]},{"start":{"row":94,"column":35},"end":{"row":94,"column":36},"action":"insert","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":1268.96875,"scrollleft":0,"selection":{"start":{"row":94,"column":36},"end":{"row":94,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":{"row":4,"state":"start","mode":"ace/mode/python"}},"timestamp":1578669603421,"hash":"084b6e544521e1cf16c6c484b8b234c9a24348fe"}