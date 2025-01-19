import React, { useState } from 'react';
import './Loginsignup.css';

import user_icon from '../Assets/profile.png';
import password_icon from '../Assets/password.png';
import email_icon from '../Assets/email.png';
import phone_icon from '../Assets/phone-call.png';

export const LoginSignup = () => {
  const [action, setAction] = useState("Sign Up");

  return (
    <div className="container">
      <div className="header">
        <div className="text">{action}</div>
        <div className="underline"></div>
      </div>
      <div className="inputs">
        {action === "Sign Up" && (
          <div className="input">
            <img src={user_icon} alt="user icon" />
            <input placeholder="Name" type="text" />
          </div>
        )}
        <div className="input">
          <img src={email_icon} alt="email icon" />
          <input placeholder="Email Id" type="email" />
        </div>
        {action === "Sign Up" && (
          <div className="input">
            <img src={phone_icon} alt="phone icon" />
            <input placeholder="Contact Number" type="tel" />
          </div>
        )}
        <div className="input">
          <img src={password_icon} alt="password icon" />
          <input placeholder="Password" type="password" />
        </div>
      </div>
      {action === "Login" && (
        <div className="forgot-password">
          Lost Password? <span>Click Here!!</span>
        </div>
      )}
      <div className="submit-container">
        <div
          className={action === "Login" ? "submit gray" : "submit"}
          onClick={() => setAction("Sign Up")}
        >
          Sign Up
        </div>
        <div
          className={action === "Sign Up" ? "submit gray" : "submit"}
          onClick={() => setAction("Login")}
        >
          Login
        </div>
      </div>
    </div>
  );
};