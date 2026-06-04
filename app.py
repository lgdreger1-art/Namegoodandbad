from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = '''
<form method="POST">
    Name bol: <input name="L">
    <input type="submit" value="Check">
</form>
{% if result %}
    <p>{{ result }}</p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        L = request.form.get('L', '').lower().strip()
        names = ['abdullah', 'abid', 'haris', 'usama']
        if L in names:
            result = 'Ek nomborer lucca khankir pola'
        else:
            result = 'Era to valo sele'
    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run()
