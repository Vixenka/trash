import './App.css';
import { useState } from 'react';
import defaultNotes from './defaultNotes.json';

function App() {
  const [notes, setNotes] = useState(() => defaultNotes)
  const [addNoteErrors, setAddNoteErrors] = useState([])

  function submitNote(event) {
    event.preventDefault()

    const title = event.target[0].value
    const description = event.target[1].value

    if (title.length !== 0 && description.length !== 0) {
      setAddNoteErrors([])
      setNotes([...notes, {
        title: title,
        description: description
      }])
    } else {
      setAddNoteErrors([
        title.length === 0 ? "Title is required" : "",
        description.length === 0 ? "Description is required" : ""
      ])
    }
  }

  function getNoteIdFromEvent(event) {
    return parseInt(event.currentTarget.parentElement.parentElement.attributes["noteid"].value);
  }

  function deleteNote(event) {
    const id = getNoteIdFromEvent(event);
    setNotes(notes.filter((_, i) => i !== id))
  }

  function editNote(event) {
    const id = getNoteIdFromEvent(event);
    const title = prompt("Edit title", notes[id].title);
    const description = prompt("Edit description", notes[id].description);

    if (title == null || description == null) {
      alert("Title and description are required")
      return;
    }

    const newNotes = [...notes];
    newNotes[id] = {
      title: title,
      description: description
    }
    setNotes(newNotes)
  }

  const renderedNotes = notes.length > 0 ? notes.map((note, i) =>
    <details key={"note" + i} noteid={i}>
      <summary>{note.title}</summary>
      <p>{note.description}</p>
      <div class="App-Note-Buttons">
        <button onClick={editNote}>Edit</button>
        <button onClick={deleteNote}>Delete</button>
      </div>
    </details>
  ) : <p class="App-No-Notes">You have any notes yet :(</p>

  return (
    <div class="App">
      <h1>Notes</h1>
      {renderedNotes}

      <form class="App-Form center-box" onSubmit={submitNote}>
        <h2>Add a new note</h2>
        <input type="text" placeholder="Title" />
        <p>{addNoteErrors[0]}</p>
        <textarea placeholder="Description"></textarea>
        <p>{addNoteErrors[1]}</p>
        <button>Add</button>
      </form>
    </div>
  );
}

export default App;
