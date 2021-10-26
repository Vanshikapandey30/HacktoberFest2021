import React from 'react'
import MyAvatar from './MyAvatar'
import MyModal from './MyModal'
import CommentInput from './CommentInput'

export default function CommentScreen({
  isOpen,
  handleClose,
  username,
  caption,
  comment,
  logo,
  index,
  handleComment,
}) {
  return (
    <MyModal handleClose={handleClose} isOpen={isOpen}>
      <div style={styles.container}>
        <div style={{ display: 'flex', padding: '10px 0' }}>
          <MyAvatar
            username={username}
            logo={logo}
            isActive={true}
            size="42px"
          />
          <h4 style={styles.caption}>
            <b>{username}</b>&nbsp;
            {caption.split('\n').map((str) => (
              <p>{str}</p>
            ))}
          </h4>
        </div>
        {comment.map(({ user, logo = '', msg }) => (
          <div style={{ display: 'flex', padding: '0 0 10px 0' }}>
            <MyAvatar username={user} logo={logo} isActive={true} size="42px" />
            <h4 style={styles.caption}>
              <b>{user}</b>&nbsp;
              {msg.split('\n').map((str) => (
                <p>{str}</p>
              ))}
            </h4>
          </div>
        ))}
        <div
          style={{
            position: 'sticky',
            bottom: 0,
            background: '#fff',
          }}
        >
          <CommentInput
            logo={logo}
            index={index}
            username={username}
            handleComment={handleComment}
          />
        </div>
      </div>
    </MyModal>
  )
}
const styles = {
  container: {
    padding: '10px',
    display: 'flex',
    flexDirection: 'column',
    background: '#fff',
    width: '50%',
    height: '100%',
    minHeight: '400px',
    minWidth: '400px',
    maxWidth: '600px',
    maxHeight: '600px',
    overflow: 'scroll',
  },
  caption: {
    fontWeight: 'normal',
    padding: '0 10px 10px 10px',
  },
}
