import React, { useRef } from 'react'
import MyAvatar from './MyAvatar'
export default function CommentInput({ index, username, logo, handleComment }) {
  const inputRef = useRef()
  return (
    <form style={styles.container} onSubmit={(e) => e.preventDefault()}>
      <MyAvatar username={username} logo={logo} size="35px" isActive={false} />
      <input
        ref={inputRef}
        type="text"
        style={styles.input}
        placeholder="Add a comment"
      />
      <button
        onClick={() => {
          if (inputRef.current.value !== '') {
            handleComment([
              index,
              {
                user: username,
                msg: inputRef.current.value,
              },
            ])
            // console.log(inputRef.current.value)
            inputRef.current.value = ''
          }
        }}
        style={{
          ...styles.buttons,
          ...{
            background: '#fff',
            color: '#0095f6',
          },
        }}
      >
        Post
      </button>
    </form>
  )
}

const styles = {
  container: { display: 'flex', padding: '10px' },
  input: {
    width: '100%',
    padding: '10px',
    border: '0px solid transparent',
    outline: 'none',
    fontSize: '16px',
    alignItem: 'center',
  },
  buttons: {
    padding: '5px 0',
    border: 'none',
    minWidth: '62px',
    maxWidth: '62px',
    fontSize: '16px',
    fontWeight: 'bold',
    borderRadius: '5px',
  },
}
