from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)
# popular_df = pickle.load('popular.pkl')
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity-scores.pkl', 'rb'))



@app.route('/')
def index():
    return render_template('index.html')

    

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('index.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)

