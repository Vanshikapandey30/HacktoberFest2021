import React, { useState } from 'react'
import Likes from './Likes'
import CommentInput from './CommentInput'
import CommentScreen from './CommentScreen'
import MyAvatar from './MyAvatar'
export default function Posts({
  logo,
  index,
  image,
  likes,
  caption,
  isLiked,
  isSaved,
  comment,
  username,
  location,
  handleToogle,
  handleComment,
}) {
  const [isExpanded, setExpanded] = useState(false)
  const [isCommentOpen, setCommentOpen] = useState(false)
  return (
    <div style={styles.container}>
      <CommentScreen
        handleComment={handleComment}
        index={index}
        username={username}
        logo={logo}
        caption={caption}
        comment={comment}
        isOpen={isCommentOpen}
        handleClose={(e) => setCommentOpen(e)}
      />
      <div style={styles.userData}>
        <div
          style={{
            display: 'flex',
            width: '100%',
            justifyContent: 'space-between',
          }}
        >
          <div style={{ display: 'flex' }}>
            <MyAvatar
              username={username}
              logo={logo}
              isActive={true}
              size="42px"
            />
            <div style={{ margin: '0 0 0 12px', maxHeight: '42px' }}>
              <div style={{ display: 'flex', alignItems: 'center' }}>
                <h3>{username}</h3>
                <h4 style={{ padding: '0 10px', color: '#0095f6' }}>Follow</h4>
              </div>
              <p style={{ color: 'grey' }}>{location}</p>
            </div>
          </div>
          <h2 style={{ padding: '0 20px' }}>...</h2>
        </div>
      </div>
      <img
        alt="404 post not found"
        src={image}
        style={styles.image}
        onDoubleClick={() => {
          handleToogle([
            index,
            { isLiked: true, likes: !isLiked ? likes + 1 : likes },
          ])
        }}
      />
      <div style={{ minHeight: '150px' }}>
        <Likes
          isLiked={isLiked}
          isSaved={isSaved}
          likes={likes}
          handleToogle={handleToogle}
          index={index}
          handleClose={(e) => setCommentOpen(e)}
        />
        <h4 style={{ padding: '0 0 10px 10px' }}>{likes} likes</h4>
        {!isExpanded &&
        (caption.split('\n').length > 2 || caption.length > 100) ? (
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <h4 style={styles.caption}>
              <b>{username}</b>&nbsp;
              {caption.split('\n', 1)[0].slice(0, 50) + ' ... '}
            </h4>
            <p
              style={{ color: 'grey', padding: '0 12px' }}
              onClick={() => setExpanded(true)}
            >
              more
            </p>
          </div>
        ) : (
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <h4 style={styles.caption}>
              <b>{username}</b>&nbsp;
              {caption.split('\n').map((str) => (
                <p>{str}</p>
              ))}
            </h4>
            {(caption.split('\n').length > 2 || caption.length > 100) && (
              <p
                style={{ color: 'grey', padding: '0 12px' }}
                onClick={() => setExpanded(false)}
              >
                hide
              </p>
            )}
          </div>
        )}
        {comment.length ? (
          <p
            onClick={() => setCommentOpen(true)}
            style={{ color: 'grey', padding: '0 10px 10px 10px' }}
          >
            View all {comment.length} comments
          </p>
        ) : (
          ''
        )}
        <p style={{ color: 'grey', padding: '0 10px 10px 10px' }}>15 sec ago</p>
      </div>
      <CommentInput
        logo={logo}
        index={index}
        username={username}
        handleComment={handleComment}
      />
    </div>
  )
}

const styles = {
  container: {
    background: '#fff',
    maxWidth: '600px',
    border: '1px solid lightgrey',
    marginBottom: '15px',
  },
  image: {
    borderTop: '1px solid lightgrey',
    borderBottom: '1px solid lightgrey',
    width: '100%',
    maxWidth: '600px',
    maxHeight: '600px',
    objectFit: 'contain',
  },
  caption: {
    fontWeight: 'normal',
    padding: '0 10px 10px 10px',
  },
  userData: {
    display: 'flex',
    maxHeight: '60px',
    padding: '14px 4px 14px 16px',
    alignItems: 'center',
  },
}
