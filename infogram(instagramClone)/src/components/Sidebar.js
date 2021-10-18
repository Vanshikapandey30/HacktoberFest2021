import React from 'react'
import MyAvatar from './MyAvatar'

export default function Sidebar({ logo, username }) {
  return (
    <div style={styles.userData}>
      <div
        style={{
          display: 'flex',
          width: '100%',
          alignItems: 'center',
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
            <h3>{username}</h3>
            <p style={{ color: 'grey' }}>{username}</p>
          </div>
        </div>
        <h4 style={{ padding: '0 10px', color: '#0095f6' }}>switch</h4>
      </div>
    </div>
  )
}

const styles = {
  userData: {
    width: '10%',
    display: 'flex',
    padding: '14px 4px 14px 16px',
    alignItems: 'center',
  },
}
