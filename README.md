# Subliminal daemon

A basic daemon for running Subliminal inside your tv-shows and movies folder.

## Docker compose and Docker Configuration

´´´
subliminal-daemon
  image: dantebarba/subliminal-daemon
  volumes:
    - "/tvshows:/tv"
    - "/movies:/movies"
    - "/logs:/tmp"
´´´
