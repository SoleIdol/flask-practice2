# author:Sole_idol
# filename: manage.py
# datetime:2020/8/18 15:41
"""
渲染模板引擎，传递参数练习
"""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

stus = {1: {'name': 'tom', 'gender': 'male', 'chinese': 90, 'math': 78},
        2: {'name': 'bob', 'gender': 'male', 'chinese': 87, 'math': 65},
        3: {'name': 'lucy', 'gender': 'female', 'chinese': 74, 'math': 73},
        4: {'name': 'lily', 'gender': 'female', 'chinese': 86, 'math': 90},
        5: {'name': 'alex', 'gender': 'male', 'chinese': 91, 'math': 77},
        6: {'name': 'john', 'gender': 'male', 'chinese': 79, 'math': 72},
        7: {'name': 'jack', 'gender': 'male', 'chinese': 60, 'math': 99},
        8: {'name': 'tomas', 'gender': 'male', 'chinese': 88, 'math': 98},
        9: {'name': 'eva', 'gender': 'female', 'chinese': 100, 'math': 85},
        10: {'name': 'ella', 'gender': 'female', 'chinese': 70, 'math': 81}}


@app.route('/')
def main():
    # print(stus.items())
    return render_template('main.html', stus=stus.items())


@app.route('/user_info/', methods=('POST', 'GET'))
def userInfo():
    if request.method == 'POST':
        name = request.form.get('name')
        gender = request.form.get('gender')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        stu = {'name': name, 'gender': gender, 'chinese': chinese, 'math': math}
        sid = int(request.form.get('sid'))
        stus[sid].update(stu)
        # print('stu信息为：',stu)
        
        # 头像上传
        head = request.files.get('head')
        # print('头像', head)
        if head != None:
            # print('运行了存储')
            head.save(f'static/img/{sid}.jpg')
        # print(stus)
        
        return render_template('user_info.html', stu=stu, sid=sid)
        # return redirect('/')
        # return render_template('main.html', stus=stus.items())
    else:
        sid = int(request.args.get('sid'))
        stu = stus[sid]
        # print(stu)
        return render_template('user_info.html', stu=stu, sid=sid)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
