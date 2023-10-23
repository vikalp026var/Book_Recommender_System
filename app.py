import pickle 
import streamlit as st 
import numpy as np 
from scipy.sparse import _csparsetools
from scipy.sparse import csr_matrix
import pandas as pd 
import numpy as np 
from sklearn.neighbors import NearestNeighbors
# import seaborn as sns 
# import matplotlib.pyplot as plt 
# %matplotlib inline 

# books=pd.read_csv('artifacts/Books.csv',sep=',',error_bad_lines=False,encoding='latin-1')
# books.rename(columns={
#     'Book-Title':'Title',
#     'Book-Author':"Author",
#     'Year-Of-Publication':'Year',
#     'Image-URL-L':'URL'
    
# },inplace=True)
# users=pd.read_csv('artifacts/Users.csv',sep=',',error_bad_lines=False,encoding='latin-1')
# ratings=pd.read_csv('artifacts/Ratings.csv',sep=',',error_bad_lines=False,encoding='latin-1')
# ratings.rename(columns={
# 'User-ID':"user_id",
#     'Book-Rating':'rating'
# },inplace=True)
# x=ratings['user_id'].value_counts()>200
# y=x[x].index
# ratings=ratings[ratings['user_id'].isin(y)]
# ratings_books=ratings.merge(books,on="ISBN")
# num_rating=ratings_books.groupby('Title')['rating'].count().reset_index()
# num_rating.rename(columns={
#     'rating':'num_of_rating'
# },inplace=True)
# final_rating=ratings_books.merge(num_rating,on='Title')
# final_rating=final_rating[final_rating['num_of_rating']>=50]
# final_rating.drop_duplicates(['user_id','Title'],inplace=True)
# book_pivot=final_rating.pivot_table(columns='user_id',index='Title',values='rating')
# book_pivot.fillna(0,inplace=True)
# book_sparse=csr_matrix(book_pivot)
# model=NearestNeighbors(algorithm='brute')
# model.fit(book_sparse)
# distance,suggestion=model.kneighbors(book_pivot.iloc[237,:].values.reshape(1,-1),n_neighbors=6)
# book_name=book_pivot.index
# pickle.dump(model,open('artifacts/model.pkl','wb'))
# pickle.dump(book_name,open('artifacts/book_name.pkl','wb'))
# pickle.dump(final_rating,open('artifacts/final_rating.pkl','wb'))
# pickle.dump(book_pivot,open('artifacts/book_pivot.pkl','wb'))



st.header("Books Recommender System using Machine Learning")
model=pickle.load(open('artifacts/model.pkl','rb'))
books_name=pickle.load(open('artifacts/book_name.pkl','rb'))
final_rating=pickle.load(open('artifacts/final_rating.pkl','rb'))
book_pivot=pickle.load(open('artifacts/book_pivot.pkl','rb'))

def fecth_poster(suggestion):
     book_name=[]
     ids_index=[]
     poster_url=[]
     for book_id in suggestion:
          book_name.append(book_pivot.index[book_id])

     for i in book_name[0]:
          ids=np.where(final_rating['Title']==i)[0][0]
          ids_index.append(ids)

     for idx in ids_index:
          url=final_rating.iloc[idx]['URL']
          poster_url.append(url)
     return poster_url

def recommend_books(book_name):
     book_list=[]
     book_id=np.where(book_pivot.index==book_name)[0][0]
     distance,suggestion=model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)
     poster_url=fecth_poster(suggestion)
     for i in range(len(suggestion)):
          books=book_pivot.index[suggestion[i]]
          for j in books:
               book_list.append(j)
     return book_list,poster_url

selected_books=st.selectbox(
     "Type or select a book",
     books_name
)
if st.button('Show Recommmendation'):
     recommendation_books,poster_url=recommend_books(selected_books)
     col1,col2,col3,col4,col5=st.columns(5)
     with col1:
          st.text(recommendation_books[1])
          st.image(poster_url[1])
     with col2:
          st.text(recommendation_books[2])
          st.image(poster_url[2])
     with col3:
          st.text(recommendation_books[3])
          st.image(poster_url[3])
     with col4:
          st.text(recommendation_books[4])
          st.image(poster_url[4])
     with col5:
          st.text(recommendation_books[5])
          st.image(poster_url[5])
          