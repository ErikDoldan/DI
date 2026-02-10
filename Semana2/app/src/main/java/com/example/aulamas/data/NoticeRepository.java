package com.example.aulamas.data;

import java.util.ArrayList;
import java.util.List;
public class NoticeRepository {

    // La "base de datos" en memoria. static para que sobreviva a todo.
    private static final List<String> notices = new ArrayList<>();

    public void addNotice(String notice) {
        notices.add(notice);
    }

    public List<String> getAllNotices() {
        return new ArrayList<>(notices);
    }

    // En data/NoticeRepository.java
    public void removeNotice(String notice) {
        notices.remove(notice);
    }
}

