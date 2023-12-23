import { useState } from "preact/hooks";
import { invoke } from "@tauri-apps/api/tauri";
import ReadingList from "./ReadingList";
import "./App.css";

function App() {

  return (
    <div class= "container" >
    <ReadingList/>
    < /div>
  );
}

export default App;
