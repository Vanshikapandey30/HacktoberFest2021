import React from 'react'
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder'
import FavoriteIcon from '@mui/icons-material/Favorite'
import CommentOutlinedIcon from '@mui/icons-material/CommentOutlined'
import TelegramIcon from '@mui/icons-material/Telegram'
import BookmarkBorderIcon from '@mui/icons-material/BookmarkBorder'
import BookmarkIcon from '@mui/icons-material/Bookmark'

import '../App.css'

export default function Likes({
  isLiked = false,
  isSaved = false,
  likes = 0,
  handleToogle,
  index,
  handleClose,
}) {
  // const [isLiked, setLiked] = useState(false)
  // const [isSaved, setSaved] = useState(false)
  return (
    <div style={styles.container}>
      <div>
        {isLiked ? (
          <FavoriteIcon
            className="iconStyles"
            style={{ fill: '#ed4956', fontSize: '30px' }}
            onClick={() => {
              handleToogle([
                index,
                {
                  isLiked: !isLiked,
                  isSaved: isSaved,
                  likes: likes - 1,
                },
              ])
            }}
          />
        ) : (
          <FavoriteBorderIcon
            className="iconStyles"
            style={styles.icon}
            onClick={() => {
              handleToogle([
                index,
                { isLiked: !isLiked, isSaved: isSaved, likes: likes + 1 },
              ])
            }}
          />
        )}
        <CommentOutlinedIcon
          onClick={() => handleClose(true)}
          className="iconStyles"
          style={styles.icon}
        />
        <TelegramIcon className="iconStyles" style={styles.icon} />
      </div>
      {isSaved ? (
        <BookmarkIcon
          style={styles.icon}
          className="iconStyles"
          onClick={() => {
            handleToogle([index, { isLiked: isLiked, isSaved: !isSaved }])
          }}
        />
      ) : (
        <BookmarkBorderIcon
          className="iconStyles"
          style={styles.icon}
          onClick={() => {
            handleToogle([index, { isLiked: isLiked, isSaved: !isSaved }])
          }}
        />
      )}
    </div>
  )
}

const styles = {
  container: {
    display: 'flex',
    width: '100%',
    justifyContent: 'space-between',
    padding: '10px 0',
  },
  icon: {
    fontSize: '30px',
  },
}
