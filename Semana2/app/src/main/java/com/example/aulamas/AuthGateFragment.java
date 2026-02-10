package com.example.aulamas;

import android.os.Bundle;
import android.view.View;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;
import com.example.aulamas.R;
import com.google.firebase.auth.FirebaseAuth;

public class AuthGateFragment extends Fragment {

    public AuthGateFragment() {
        // Puedes dejar el layout que se crea por defecto o uno vacío
        super(R.layout.fragment_auth_gate);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // PREGUNTA CLAVE: ¿Hay alguien logueado?
        if (FirebaseAuth.getInstance().getCurrentUser() != null) {
            // SI -> Vamos directos al Home
            NavHostFragment.findNavController(this).navigate(R.id.action_gate_to_home);
        } else {
            // NO -> Vamos al Login
            NavHostFragment.findNavController(this).navigate(R.id.action_gate_to_login);
        }
    }
}