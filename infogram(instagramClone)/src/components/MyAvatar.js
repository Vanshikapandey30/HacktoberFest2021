import React from 'react'
import { Avatar } from '@material-ui/core'

export default function MyAvatar({ username, logo, isActive, size }) {
  return (
    <Avatar
      alt={username}
      src={logo}
      style={{
        maxWidth: size,
        maxHeight: size,
        objectFit: 'contain',
        border: isActive ? '3px solid #f6f' : 'none',
      }}
    />
  )
}
