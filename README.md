# Movie Recommendation Engine 2023
Building a Movie Recommendation Engine using Python and MERN stack

Link to the refernce page which I will be using as my frontend - https://netflix-clone-cd47e.web.app/

Python Notebook - https://colab.research.google.com/drive/1249bljluGnQpYDN491Lc6z6fcRHMUJcT?usp=sharing

Refrence@ - http://surl.li/flqak

Recommender System is a system that seeks to predict or filter preferences according to the user’s choices. Recommender systems are utilized in a variety of areas including movies, music, news, books, research articles, search queries, social tags, and products in general. 
Recommender systems produce a list of recommendations in any of the two ways – 
 
Collaborative filtering: Collaborative filtering approaches build a model from the user’s past behavior (i.e. items purchased or searched by the user) as well as similar decisions made by other users. This model is then used to predict items (or ratings for items) that users may have an interest in. This makes better overall user experience.

![Colaborative filtering II](https://user-images.githubusercontent.com/95162790/170810992-c6831c6c-815b-439c-a9c3-a24821b4a24e.jpg)

![Colaborative filtering I](https://user-images.githubusercontent.com/95162790/170810974-a225d0cc-0cd7-4902-870a-8d85d19cb34d.jpg)

Content-based filtering: Content-based filtering approaches uses a series of discrete characteristics of an item in order to recommend additional items with similar properties. Content-based filtering methods are totally based on a description of the item and a profile of the user’s preferences. It recommends items based on the user’s past preferences.

We are using Collaborative filtering technique for results.

It gives result on the basis of cosine similarities.

In the CSV file, we have following attributes -
Rank,Title,Genre,Description,Director,Actors,Year,Runtime (Minutes),Rating,Votes,Revenue (Millions),Metascore

And on the basis of Director, Actors,and Genre we will be recommending movies to users.

Thank you for visiting :)

