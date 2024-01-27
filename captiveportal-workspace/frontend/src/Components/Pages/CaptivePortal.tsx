import * as React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import { DetailInterface } from "../../Models/IDetail";
import ThemeProvider from "@mui/material/styles/ThemeProvider";
import FormGroup from "@mui/material/FormGroup";
import Checkbox from "@mui/material/Checkbox";
import FormControlLabel from "@mui/material/FormControlLabel";
import Snackbar from "@mui/material/Snackbar";
import Alert from "@mui/material/Alert";
import { useSearchParams } from "react-router-dom";
import { blue, pink } from "@mui/material/colors";
import { createTheme } from "@mui/material/styles";
import WifiIcon from "@mui/icons-material/Wifi";

const theme = createTheme({
  palette: {
    primary: {
      main: pink[500],
    },
    secondary: {
      main: blue[500],
    },
  },
});

function CaptivePortalPage() {
  const commonStyles = {
    bgcolor: "background.paper",
    borderColor: "text.primary",
    minWidth: "300px",
    margin: "0 auto",
    padding: "0 20px",
    height: "100%",
    boxShadow: "1px 2px 9px #9999",
    borderRadius: "16px",
  };

  const [success, setSuccess] = React.useState(false);
  const [error, setError] = React.useState(false);
  const handleClose = (
    event?: React.SyntheticEvent | Event,
    reason?: string,
  ) => {
    if (reason === "clickaway") {
      return;
    }
    setSuccess(false);
    setError(false);
  };

  const [agree, setAgree] = React.useState(false);
  const [agree_color, setAgree_color] = React.useState("#000000");

  const [queryParameters] = useSearchParams();

  const [detail, setDetail] = React.useState<Partial<DetailInterface>>({
    Ap_mac: queryParameters.get("ap_mac") || "",
    Ap_name: queryParameters.get("ap_name") || "",
    Authorize_url: queryParameters.get("authorize_url") || "",
    Site_name: queryParameters.get("site_name") || "",
    Ssid: queryParameters.get("ssid") || "",
    Wlan_id: queryParameters.get("wlan_id") || "",
    Client_mac: queryParameters.get("client_mac") || "",
    Url: queryParameters.get("url") || "",
    Authorize_min: 525600,
    Download_kbps: 0,
    Upload_kbps: 0,
    Quota_mbytes: 0,
  });

  function handleInputChange(e: React.ChangeEvent<HTMLInputElement>): void {
    const id = e.target.id as keyof typeof detail;
    const { value } = e.target;
    setDetail({ ...detail, [id]: value });
  }

  function handleSubmitClick() {
    let data = {
      ...detail,
    };

    console.log(data);

    const apiUrl = `${process.env.REACT_APP_BACKEND_API}/auth/juniper`;
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "CF-Access-Client-Id": `${process.env.REACT_APP_CF_ACCESS_CLIENT_ID}`,
        "CF-Access-Client-Secret": `${process.env.REACT_APP_CF_ACCESS_CLIENT_SECRET}`,
      },
      body: JSON.stringify(data),
    };

    fetch(apiUrl, requestOptions)
      .then((response) => response.json())
      .then((res) => {
        console.log(res);
        if (res.data) {
          setSuccess(true);
          setTimeout(() => {
            window.location.href = "/welcome";
          }, 1500);
        } else {
          setError(true);
        }
      });
  }

  return (
    <div>
      <Snackbar
        open={success}
        autoHideDuration={6000}
        onClose={handleClose}
        anchorOrigin={{ vertical: "bottom", horizontal: "center" }}
      >
        <Alert onClose={handleClose} severity="success">
          Success
        </Alert>
      </Snackbar>
      <Snackbar
        open={error}
        autoHideDuration={6000}
        onClose={handleClose}
        anchorOrigin={{ vertical: "bottom", horizontal: "center" }}
      >
        <Alert onClose={handleClose} severity="error">
          Something was wrong!
        </Alert>
      </Snackbar>
      <div
        style={{
          position: "absolute",
          left: "50%",
          top: "50%",
          transform: "translate(-50%, -50%)",
        }}
      >
        <Container sx={{ display: "flex", justifyContent: "center" }}>
          <Box sx={{ ...commonStyles }}>
            <Box sx={{ display: "flex" }}>
              <WifiIcon
                color="primary"
                sx={{
                  fontSize: 50,
                  marginTop: "30px",
                  marginLeft: "auto",
                  marginRight: "auto",
                  width: "50%",
                }}
              />
            </Box>
            <Box
              sx={{
                display: "block",
                marginTop: 1,
                marginLeft: "auto",
                marginRight: "auto",
                flexGrow: 1,
              }}
            >
              <Typography variant="h4" sx={{ textAlign: "center" }}>
                Internet Access Portal
              </Typography>
            </Box>

            <Typography
              variant="subtitle1"
              sx={{ marginTop: 4, marginBottom: 1 }}
            >
              Information
            </Typography>
            <Box
              sx={{
                display: "flex",
                maxWidth: "calc(100% - 20px)",
                minWidth: "100%",
              }}
            >
              <Box sx={{ marginRight: 0.5 }}>
                <TextField
                  id="Firstname"
                  label="Firstname"
                  variant="outlined"
                  size="small"
                  required
                  onChange={handleInputChange}
                />
              </Box>
              <Box sx={{ marginLeft: 0.5 }}>
                <TextField
                  id="Lastname"
                  label="Lastname"
                  variant="outlined"
                  size="small"
                  required
                  onChange={handleInputChange}
                />
              </Box>
            </Box>

            <TextField
              id="Company"
              label="Company"
              variant="outlined"
              size="small"
              required
              sx={{ display: "flex", marginTop: 1.5 }}
              onChange={handleInputChange}
            />

            <TextField
              id="Email"
              label="Email"
              variant="outlined"
              size="small"
              sx={{ display: "flex", marginTop: 1.5 }}
              required
              onChange={handleInputChange}
            />

            <FormGroup>
              <FormControlLabel
                control={
                  <Checkbox
                    onChange={() => {
                      setAgree(!agree);
                    }}
                    sx={{ "& .MuiSvgIcon-root": { fontSize: 18 } }}
                  />
                }
                label={
                  <>
                    I agree to&nbsp;
                    <a
                      href="/termsconditions"
                      style={{ textDecoration: "none", color: agree_color }}
                      onMouseOver={() => {
                        setAgree_color("#2196f3");
                      }}
                      onMouseOut={() => {
                        setAgree_color("#000000");
                      }}
                    >
                      <b>Terms & Conditions</b>
                    </a>
                  </>
                }
              />
            </FormGroup>

            <ThemeProvider theme={theme}>
              <Box
                sx={{
                  display: "flex",
                  justifyContent: "center",
                  margin: 3,
                  marginBottom: 1,
                }}
              >
                <Button
                  variant="contained"
                  color="secondary"
                  disabled={!agree}
                  onClick={handleSubmitClick}
                  sx={{ marginBottom: 1 }}
                >
                  SUBMIT
                </Button>
              </Box>
            </ThemeProvider>
          </Box>
        </Container>
      </div>
    </div>
  );
}
export default CaptivePortalPage;
