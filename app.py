import streamlit as st
import pickle
new_df = pickle.load(open('/content/movies.pkl', 'rb'))
similar = pickle.load(open('/content/similarity.pkl', 'rb'))
cv = pickle.load(open('/content/vec.pkl', 'rb'))
def recommend(movies):
  if movies not in new_df['title'].values:
        return ["Movie not found."]
  index=new_df[new_df['title']==movies].index[0] 
  distance=sorted(list(enumerate(similar[index])),reverse=True,key=lambda vec:vec[1])
  recommended_movies = []
  for i in distance[1:6]:  
        recommended_movies.append(new_df.iloc[i[0]].title)
  return recommended_movies
def main():
    st.title("🎬 Movie Recommendation System")
    user_input = st.selectbox("Choose a movie to get recommendations:", new_df['title'].values)

    if st.button("Recommend"):
        recommendations = recommend(user_input)
        st.subheader("Top 5 Recommendations:")
        for i, movie in enumerate(recommendations, start=1):
            st.write(f"{i}. {movie}")

if __name__ == '__main__':
    main()