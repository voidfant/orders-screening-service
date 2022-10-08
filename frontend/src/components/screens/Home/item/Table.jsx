import React from 'react'
import axios from 'axios'

const Table = () => {
  const initialValue = [
    { 
      order_id: 0,
      order_number: 0,
      cost_usd: 0,
      cost_rub: 0,
      order_date: ""
    }];

  const [data, setData] = React.useState(initialValue);

  const fetchData = React.useCallback(async () => {
      const url = '/data';
      const result = await axios.get(url);

      setData(result.data);
      console.log([result.data])
  }, []);



  React.useEffect(() => {
      fetchData();
  }, [fetchData]);
    
  return (
      <div className="bg-gray-700 overflow-x-auto overflow-y-scroll relative shadow-md sm:rounded-sm" style={{height:300}}>
        <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
            <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" className="py-3 px-6">
                        №
                    </th>
                    <th scope="col" className="py-3 px-6">
                        Заказ №
                    </th>
                    <th scope="col" className="py-3 px-6">
                        Стоимость, $
                    </th>
                    <th scope="col" className="py-3 px-6">
                        Срок поставки
                    </th>
                </tr>
            </thead>
            <tbody>
              {data.map((item, i) => {
              return(
              <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700" key={i}>
                <td className="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                  {item.order_id}
                </td>
                <td className="py-4 px-6">
                  {item.order_number}
                </td>
                <td className="py-4 px-6">
                  {item.cost_usd}
                </td>
                <td className="py-4 px-6">
                  {item.order_date}
                </td>
              </tr>
            )
            })}
            </tbody>
        </table>
      </div>
  )
  }
  


export default Table

// import React from "react";
// import { useTable } from "react-table";

// export default function Table({ columns, data }) {
//   // Use the useTable Hook to send the columns and data to build the table
//   const {
//     getTableProps, // table props from react-table
//     getTableBodyProps, // table body props from react-table
//     headerGroups, // headerGroups, if your table has groupings
//     rows, // rows for the table based on the data passed
//     prepareRow // Prepare the row (this function needs to be called for each row before getting the row props)
//   } = useTable({
//     columns,
//     data
//   });

//   /* 
//     Render the UI for your table
//     - react-table doesn't have UI, it's headless. We just need to put the react-table props from the Hooks, and it will do its magic automatically
//   */
//   return (
//     <table {...getTableProps()}>
//       <thead>
//         {headerGroups.map(headerGroup => (
//           <tr {...headerGroup.getHeaderGroupProps()}>
//             {headerGroup.headers.map(column => (
//               <th {...column.getHeaderProps()}>{column.render("Header")}</th>
//             ))}
//           </tr>
//         ))}
//       </thead>
//       <tbody {...getTableBodyProps()}>
//         {rows.map((row, i) => {
//           prepareRow(row);
//           return (
//             <tr {...row.getRowProps()}>
//               {row.cells.map(cell => {
//                 return <td {...cell.getCellProps()}>{cell.render("Cell")}</td>;
//               })}
//             </tr>
//           );
//         })}
//       </tbody>
//     </table>
//   );
// }