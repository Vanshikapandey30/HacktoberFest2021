import React, { useState } from 'react'

import '../App.css'

import HomeIcon from '@mui/icons-material/Home'
import HomeOutlinedIcon from '@mui/icons-material/HomeOutlined'
import AddReactionOutlinedIcon from '@mui/icons-material/AddReactionOutlined'
import AddReactionIcon from '@mui/icons-material/AddReaction'
import AddBoxIcon from '@mui/icons-material/AddBox'
import AddBoxOutlinedIcon from '@mui/icons-material/AddBoxOutlined'
import FavoriteIcon from '@mui/icons-material/Favorite'
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder'
import { Avatar } from '@material-ui/core'

export default function Footer({ username, logo, handleUploader }) {
  const [screenName, setScreenName] = useState('home')
  return (
    <div style={styles.container}>
      {screenName === 'home' ? (
        <HomeIcon
          style={{ ...styles.icons, ...{ fontSize: '33px', fill: '#f09' } }}
        />
      ) : (
        <HomeOutlinedIcon
          style={styles.icons}
          className="FooterIcons"
          onClick={() => setScreenName('home')}
        />
      )}
      {screenName === 'search' ? (
        <AddReactionIcon
          style={{ ...styles.icons, ...{ fontSize: '33px', fill: '#fa0' } }}
        />
      ) : (
        <AddReactionOutlinedIcon
          style={styles.icons}
          className="FooterIcons"
          onClick={() => setScreenName('search')}
        />
      )}
      {screenName === 'add' ? (
        <AddBoxIcon
          onClick={() => {
            handleUploader(['uploader', true])
          }}
          style={{ ...styles.icons, ...{ fontSize: '33px', fill: '#0095f6' } }}
        />
      ) : (
        <AddBoxOutlinedIcon
          style={styles.icons}
          className="FooterIcons"
          onClick={() => {
            setScreenName('add')
            handleUploader(['uploader', true])
          }}
        />
      )}
      {screenName === 'fav' ? (
        <FavoriteIcon
          style={{ ...styles.icons, ...{ fontSize: '33px', fill: '#ed4956' } }}
        />
      ) : (
        <FavoriteBorderIcon
          style={styles.icons}
          className="FooterIcons"
          onClick={() => setScreenName('fav')}
        />
      )}
      <Avatar
        className="FooterIcons"
        alt={username}
        src={logo}
        style={{
          maxWidth: '30px',
          maxHeight: '30px',
          objectFit: 'contain',
          border: screenName === 'user' ? '3px solid #f3f' : 'none',
        }}
        onClick={() => setScreenName('user')}
      />
    </div>
  )
}

const styles = {
  container: {
    position: 'sticky',
    bottom: '0',
    zIndex: '1000',
    display: 'flex',
    background: '#fff',
    padding: '0 20px',
    minHeight: '52px',
    border: '1px solid lightgrey',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  icons: {
    fontSize: '30px',
  },
}
