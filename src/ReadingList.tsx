import { useState } from "preact/hooks";
import preactLogo from "./assets/preact.svg";
import { invoke } from "@tauri-apps/api/tauri";
import { open } from '@tauri-apps/api/dialog';
import get_file_name from "./utils/get_file_name";

type queElement = {
  name: string,
  file_path: string
}

function ReadingList() {
  const [que, addToQue] = useState<queElement[]>([])
  async function addFile() {
     const file_path = await open({
            multiple: false,
            directory: false,
            filters: [{
              name: 'Book',
              extensions: ['pdf']
            }]
        });
     if (Array.isArray(file_path) || file_path === null ) {
       return Promise.reject("Selected zero or multiple files'")
     }
    const name = await get_file_name(file_path)
        addToQue(()=> {
          let new_que = [...que]
          new_que.push({
            name,
file_path
          })
          return new_que
        })
  }

  const books = que.map((que_element: queElement
  )=> <p>{que_element.name}</p>)
  
  return (
    <div class= "reading_list" >
      <div>
        <button onclick={addFile}>Add</button>
        <button>Next</button>
      </div>
      <div>
        {books}
      </div>
    </div>
  );
}

export default ReadingList;
