import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [slots, setSlots] = useState([]);
  const [bookedSlots, setBookedSlots] = useState([]);
  const [username, setUsername] = useState("");

  useEffect(() => {
    loadSlots();
    loadBookedSlots();
  }, []);

  const loadSlots = async () => {
    const res = await axios.get("http://127.0.0.1:8000/slots");
    setSlots(res.data);
  };

  const loadBookedSlots = async () => {
    const res = await axios.get("http://127.0.0.1:8000/booked");
    setBookedSlots(res.data);
  };

  const bookSlot = async (id) => {

    if(username === ""){
      alert("Enter your name first");
      return;
    }

    await axios.post(`http://127.0.0.1:8000/book/${id}`, {
      username: username
    });

    setUsername("");

    loadSlots();
    loadBookedSlots();
  };

  return (
    <div className="container">

      <h1 className="title">Slot Booking System</h1>

      <h3>Enter Name</h3>
      <input
        value={username}
        onChange={(e)=>setUsername(e.target.value)}
        placeholder="Enter your name"
      />

      <h2>Available Slots</h2>

      {slots.map((slot)=>(
        <div className="slot" key={slot.id}>
          {slot.slot_time}

          <button
            className="book-btn"
            onClick={()=>bookSlot(slot.id)}
          >
            Book
          </button>
        </div>
      ))}

      <h2>Booked Slots</h2>

      {bookedSlots.map((slot)=>(
        <div className="booked" key={slot.id}>
          {slot.slot_time} - Booked by {slot.username}
        </div>
      ))}

    </div>
  );
}

export default App;