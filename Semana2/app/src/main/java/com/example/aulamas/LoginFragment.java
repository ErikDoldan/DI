package com.example.aulamas;

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

public class LoginFragment extends Fragment {

    public LoginFragment() {
        super(R.layout.fragment_login);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // 1. INICIALIZAR VIEWMODEL (Con Factory porque necesita Repo)
        AuthRepository repo = new AuthRepository();
        AuthViewModelFactory factory = new AuthViewModelFactory(repo);
        AuthViewModel vm = new ViewModelProvider(this, factory).get(AuthViewModel.class);

        // 2. REFERENCIAS UI
        TextInputLayout tilEmail = view.findViewById(R.id.tilEmail);
        TextInputEditText etEmail = view.findViewById(R.id.etEmail);
        TextInputLayout tilPass = view.findViewById(R.id.tilPass);
        TextInputEditText etPass = view.findViewById(R.id.etPass);
        MaterialButton btnLogin = view.findViewById(R.id.btnLogin);
        MaterialButton btnRegister = view.findViewById(R.id.btnGoRegister);
        CircularProgressIndicator progress = view.findViewById(R.id.progress);

        // 3. OBSERVAR ESTADOS (Lo que dice el ViewModel)

        // A) Loading: Bloqueamos botones y mostramos rueda
        vm.getLoading().observe(getViewLifecycleOwner(), isLoading -> {
            progress.setVisibility(isLoading ? View.VISIBLE : View.GONE);
            btnLogin.setEnabled(!isLoading);
            btnRegister.setEnabled(!isLoading);
        });

        // B) Error: Mostramos Snackbar rojo
        vm.getErrorMessage().observe(getViewLifecycleOwner(), msg -> {
            if (msg != null) {
                Snackbar.make(view, msg, Snackbar.LENGTH_LONG).setBackgroundTint(0xFFB71C1C).show();
            }
        });

        // C) Navegación: Si login OK, vamos a Home
        vm.getNavEvent().observe(getViewLifecycleOwner(), event -> {
            if ("HOME".equals(event)) {
                NavHostFragment.findNavController(this).navigate(R.id.action_login_to_home);
                vm.consumeNavEvent(); // Limpiamos el evento
            }
        });

        // 4. LISTENERS (Botones)

        // Ir a registrarse
        btnRegister.setOnClickListener(v ->
                NavHostFragment.findNavController(this).navigate(R.id.action_login_to_register)
        );

        // Intentar Login
        btnLogin.setOnClickListener(v -> {
            // Limpiar errores previos
            tilEmail.setError(null);
            tilPass.setError(null);

            String email = etEmail.getText().toString().trim();
            String pass = etPass.getText().toString().trim();

            // Validación Local (Reglas básicas)
            boolean isValid = true;
            if (email.isEmpty()) {
                tilEmail.setError("El email es obligatorio");
                isValid = false;
            }
            if (pass.isEmpty()) {
                tilPass.setError("Escribe la contraseña");
                isValid = false;
            }

            // Si pasa la validación local, llamamos a Firebase
            if (isValid) {
                vm.login(email, pass);
            }
        });
    }
}