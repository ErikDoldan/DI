package com.example.aulamas; // Tu paquete

import android.os.Bundle;
import android.view.View;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.fragment.NavHostFragment;

import com.example.aulamas.R;
import com.example.aulamas.data.AuthRepository;
import com.example.aulamas.viewmodel.AuthViewModel;
import com.example.aulamas.viewmodel.AuthViewModelFactory;

import com.google.android.material.button.MaterialButton;
import com.google.android.material.progressindicator.CircularProgressIndicator;
import com.google.android.material.snackbar.Snackbar;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

public class RegisterFragment extends Fragment {

    public RegisterFragment() {
        super(R.layout.fragment_register);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // 1. VM
        AuthRepository repo = new AuthRepository();
        AuthViewModelFactory factory = new AuthViewModelFactory(repo);
        AuthViewModel vm = new ViewModelProvider(this, factory).get(AuthViewModel.class);

        // 2. UI
        TextInputLayout tilEmail = view.findViewById(R.id.tilEmail);
        TextInputEditText etEmail = view.findViewById(R.id.etEmail);
        TextInputLayout tilPass = view.findViewById(R.id.tilPass);
        TextInputEditText etPass = view.findViewById(R.id.etPass);
        MaterialButton btnRegister = view.findViewById(R.id.btnRegister);
        MaterialButton btnGoLogin = view.findViewById(R.id.btnGoLogin);
        CircularProgressIndicator progress = view.findViewById(R.id.progress);

        // 3. OBSERVERS
        vm.getLoading().observe(getViewLifecycleOwner(), isLoading -> {
            progress.setVisibility(isLoading ? View.VISIBLE : View.GONE);
            btnRegister.setEnabled(!isLoading);
        });

        vm.getErrorMessage().observe(getViewLifecycleOwner(), msg -> {
            if (msg != null) {
                Snackbar.make(view, msg, Snackbar.LENGTH_LONG).setBackgroundTint(0xFFB71C1C).show();
            }
        });

        vm.getNavEvent().observe(getViewLifecycleOwner(), event -> {
            if ("HOME".equals(event)) {
                NavHostFragment.findNavController(this).navigate(R.id.action_register_to_home);
                vm.consumeNavEvent();
            }
        });

        // 4. LISTENERS

        // Volver a login (Usamos popBackStack para volver atrás limpiamente)
        btnGoLogin.setOnClickListener(v ->
                NavHostFragment.findNavController(this).popBackStack()
        );

        // Crear Cuenta
        btnRegister.setOnClickListener(v -> {
            tilEmail.setError(null);
            tilPass.setError(null);

            String email = etEmail.getText().toString().trim();
            String pass = etPass.getText().toString().trim();

            boolean isValid = true;
            if (email.isEmpty() || !email.contains("@")) {
                tilEmail.setError("Email no válido");
                isValid = false;
            }
            if (pass.length() < 6) {
                tilPass.setError("Mínimo 6 caracteres");
                isValid = false;
            }

            if (isValid) {
                vm.register(email, pass);
            }
        });
    }
}