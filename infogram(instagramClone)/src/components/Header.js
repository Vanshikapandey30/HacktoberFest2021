import React from 'react'

export default function Header() {
  return (
    <div style={styles.container}>
      <div style={styles.inner}>
        <h1
          style={{
            fontFamily: 'logoFont',
            fontWeight: 'normal',
            fontSize: '24px',
          }}
        >
          Infogram
        </h1>
        <div style={styles.buttonContainer}>
          <button
            style={{
              ...styles.buttons,
              ...{
                background: '#0095f6',
                color: '#fff',
              },
            }}
          >
            Log in
          </button>
          <button
            style={{
              ...styles.buttons,
              ...{
                background: '#fff',
                color: '#0095f6',
              },
            }}
          >
            Sign up
          </button>
        </div>
      </div>
    </div>
  )
}

const styles = {
  container: {
    position: 'sticky',
    top: '0',
    zIndex: '1000',
    background: '#fff',
    padding: '0 20px',
    minHeight: '52px',
    display: 'grid',
    justifyContent: 'center',
    border: '1px solid lightgrey',
  },
  inner: {
    maxWidth: '930px',
    width: '100vw',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  buttonContainer: {
    display: 'flex',
    justifyContent: 'space-evenly',
    minWidth: '130px',
    width: '100%',
    maxWidth: '160px',
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
