import React from 'react'


const LayoutU = ({graph, counter, table}) => {
  return (
    <div className='bg-white grid grid-cols-2 gap-4'>
        <div className='bg-green-300 shadow-sm min-h-[100px] col-span-2 row-span-2'/>
        <div className='row-span-2'>{graph}</div>
        <div className=''>{counter}</div>
        <div className=''>{table}</div>
    </div>
  )
}

export default LayoutU