package com.example.aulamas.data;
import com.google.firebase.auth.FirebaseAuth;
public class AuthRepository {

        // Obtenemos la instancia de Firebase Auth
        private final FirebaseAuth auth = FirebaseAuth.getInstance();

        public FirebaseAuth getAuth() {
            return auth;
        }
    }

