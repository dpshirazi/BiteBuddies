import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBMLGLGOG7a-Y6JAdeSKwyHctBuwE6TH04",
  authDomain: "bitebuddies-8d6f6.firebaseapp.com",
  projectId: "bitebuddies-8d6f6",
  storageBucket: "bitebuddies-8d6f6.firebasestorage.app",
  messagingSenderId: "616497555302",
  appId: "1:616497555302:web:6548978978ef3ce72d0aa7",
  measurementId: "G-NNJCNZM287"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);

// Example of Firebase Authentication logic
function signUp(email, password) {
  createUserWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      const user = userCredential.user;
      console.log("User created:", user);
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      console.error(`Error (${errorCode}): ${errorMessage}`);
    });
}

// Example usage
signUp('user@example.com', 'password123');
