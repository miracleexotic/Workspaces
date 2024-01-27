import { Box, Typography } from "@mui/material";
import { Container } from "@mui/system";

function ForescoutRedirectPage() {
  const commonStyles = {
    bgcolor: "background.paper",
    borderColor: "text.primary",
    minWidth: "300px",
    margin: "0 auto",
    height: "100%",
    boxShadow: "1px 2px 9px #9999",
    padding: "2.5em",
    borderRadius: "16px",
  };

  return (
    <div>
      <Container sx={{ display: "flex", justifyContent: "center" }}>
        <Box sx={{ ...commonStyles, marginTop: 5 }}>
          <Box sx={{ marginBottom: 0 }}>
            <img src="/static/images/logo.png" alt="NT" />
            <Typography variant="body1" sx={{ marginTop: 3 }}>
              <b>กรุณาติดตั้งโปรแกรมด้านล่างก่อนเข้าใช้งาน</b>
            </Typography>
            <a href="/static/forescout/SC-CgECXCcTPzQIGRIKWMvBrA1WHrAegxgDaMK1bde_+fn0WUoJV3sEAAE-.exe">
              Download
            </a>
          </Box>
        </Box>
      </Container>
    </div>
  );
}

export default ForescoutRedirectPage;
