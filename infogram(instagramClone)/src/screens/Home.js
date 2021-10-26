import React from 'react'
import Posts from '../components/Posts'

export default function Home({ data, handleToogle, handleComment }) {
  return (
    <div>
      {data.map(
        (
          {
            logo,
            image,
            likes,
            comment,
            caption,
            isLiked,
            isSaved,
            username,
            location,
          },
          index,
        ) => (
          <Posts
            key={index}
            username={username}
            location={location}
            caption={caption}
            logo={logo}
            image={image}
            isLiked={isLiked}
            isSaved={isSaved}
            handleToogle={handleToogle}
            handleComment={handleComment}
            index={index}
            likes={likes}
            comment={comment}
          />
        ),
      )}
    </div>
  )
}
