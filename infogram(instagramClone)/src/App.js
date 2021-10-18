import './App.css'
import Header from './components/Header'
import Footer from './components/Footer'
import Uploader from './components/Uploader'
import Home from './screens/Home'
import React, { useState } from 'react'
import Sidebar from './components/Sidebar'

function App() {
  const [isUploaderOpen, setUploaderOpen] = useState(false)
  const handleUploader = (e) => {
    setUploaderOpen(e)
  }
  const [data, setData] = useState([
    {
      username: 'srinivasTheDeveloper',
      location: 'chennai',
      caption:
        'his blah blah blah content his blah blah blah content his blah blah blah content his blah blah blah content his blah blah blah content \nhis blah blah blah content \n.\n.\n.\nhis blah blah blah content \nhis blah blah blah content \n',
      logo: 'image.jpg',
      image: 'image.jpg',
      isLiked: false,
      isSaved: false,
      likes: 100,
      comment: [{ user: 'username', msg: 'comment' }],
    },
    {
      username: 'srinivasTheDeveloper',
      location: 'mumbai',
      caption: 'his blah blah blah content2',
      logo: 'image.jpg',
      image: 'image.jpg',
      isLiked: true,
      isSaved: true,
      likes: 10,
      comment: [{ user: 'username1', msg: 'comment1' }],
    },
  ])
  const handleToogle = (e) => {
    let update = [...data]
    update[e[0]] = { ...update[e[0]], ...e[1] }
    setData(update)
  }
  const handleUpload = (e) => {
    setData([...data, e])
  }
  const handleComment = (e) => {
    let update = [...data]
    update[e[0]]['comment'].push(e[1])
    setData(update)
    // console.log(data)
  }
  return (
    <div className="app">
      <Header />
      <div style={{ display: 'grid', placeItems: 'center' }}>
        <div style={{ display: 'flex', alignItems: 'flex-start' }}>
          <div className="appHome">
            <Home
              data={data}
              handleToogle={handleToogle}
              handleComment={handleComment}
            />
          </div>
          <Sidebar username="SrinivasTheDeveloper" logo={'image.jpg'} />
        </div>
        <Uploader
          isOpen={isUploaderOpen}
          handleClose={handleUploader}
          handleUpload={handleUpload}
        />
      </div>
      <Footer
        username="SrinivasTheDeveloper"
        logo={'image.jpg'}
        isUploaderOpen={isUploaderOpen}
        handleUploader={handleUploader}
      />
    </div>
  )
}

export default App
