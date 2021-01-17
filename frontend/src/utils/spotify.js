export function authSignIn() {
  console.log("Redirect to Spotify login");
  window.open(
    "https://accounts.spotify.com/en/authorize?client_id=eb0421952dd6477ab01780be94ede588&response_type=code&redirect_uri=http:%2F%2Flocalhost:3000%2Fmood&scope=user-read-private%20user-read-email%20user-read-recently-played&state=34fFs29kd09",
    "_self"
  );
}
