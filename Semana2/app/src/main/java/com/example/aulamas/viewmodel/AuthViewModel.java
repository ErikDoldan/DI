package com.example.aulamas.viewmodel;


import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.aulamas.data.AuthRepository;
import com.google.firebase.auth.FirebaseAuth;

public class AuthViewModel extends ViewModel {

    private final FirebaseAuth auth;

    // ESTADOS DE LA UI
    private final MutableLiveData<Boolean> _loading = new MutableLiveData<>(false);
    private final MutableLiveData<String> _errorMessage = new MutableLiveData<>(null);

    // EVENTO DE NAVEGACIÓN ("HOME" si todo va bien)
    private final MutableLiveData<String> _navEvent = new MutableLiveData<>(null);

    // Constructor que recibe el repositorio
    public AuthViewModel(AuthRepository repo) {
        this.auth = repo.getAuth();
    }

    // Getters para observar
    public LiveData<Boolean> getLoading() { return _loading; }
    public LiveData<String> getErrorMessage() { return _errorMessage; }
    public LiveData<String> getNavEvent() { return _navEvent; }

    // Consumir evento (para que no navegue dos veces al rotar)
    public void consumeNavEvent() { _navEvent.setValue(null); }

    // --- LÓGICA DE LOGIN ---
    public void login(String email, String pass) {
        _errorMessage.setValue(null); // Limpiar errores previos
        _loading.setValue(true);      // Mostrar carga

        auth.signInWithEmailAndPassword(email, pass)
                .addOnCompleteListener(task -> {
                    _loading.setValue(false); // Ocultar carga pase lo que pase
                    if (task.isSuccessful()) {
                        _navEvent.setValue("HOME"); // Éxito -> Navegar
                    } else {
                        // Error -> Mostrar mensaje amigable
                        _errorMessage.setValue(parseAuthError(task.getException()));
                    }
                });
    }

    // --- LÓGICA DE REGISTRO ---
    public void register(String email, String pass) {
        _errorMessage.setValue(null);
        _loading.setValue(true);

        auth.createUserWithEmailAndPassword(email, pass)
                .addOnCompleteListener(task -> {
                    _loading.setValue(false);
                    if (task.isSuccessful()) {
                        _navEvent.setValue("HOME");
                    } else {
                        _errorMessage.setValue(parseAuthError(task.getException()));
                    }
                });
    }

    // Método para traducir errores técnicos a español (UX)
    private String parseAuthError(Exception e) {
        if (e == null) return "Error desconocido";
        String msg = e.getMessage();
        if (msg != null) {
            if (msg.contains("password")) return "Contraseña incorrecta o muy corta";
            if (msg.contains("no user record")) return "No existe cuenta con este email";
            if (msg.contains("already in use")) return "Este email ya está registrado";
            if (msg.contains("network")) return "Error de red. Revisa tu conexión";
            if (msg.contains("badly formatted")) return "El email no tiene formato correcto";
        }
        return "No se pudo completar la operación: " + msg;
    }
}