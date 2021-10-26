import { Modal } from '@mui/material'
import React from 'react'

export default function MyModal({ children, handleClose, isOpen }) {
  return (
    <Modal
      onBackdropClick={() => handleClose(false)}
      style={{ display: 'grid', placeItems: 'center' }}
      open={isOpen}
      onClose={() => handleClose(false)}
    >
      {children}
    </Modal>
  )
}
