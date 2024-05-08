import { Typography } from "@mui/material";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";

function WelcomePage() {
  return (
    <div
      style={{
        position: "absolute",
        left: "50%",
        top: "50%",
        transform: "translate(-50%, -50%)",
      }}
    >
      <Container
        sx={{
          display: "flex",
          justifyContent: "center",
        }}
      >
        <Box sx={{ display: "blox", justifyContent: "center" }}>
          <Typography
            variant="h3"
            sx={{
              background: "linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)",
              color: "#fff",
            }}
          >
            <b>WELCOME</b>
          </Typography>
        </Box>
      </Container>
    </div>
  );
}

export default WelcomePage;
