import { Box, Typography } from "@mui/material";
import { Container } from "@mui/system";

function TermsConditionsPage() {
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
          <Box sx={{ marginBottom: 1 }}>
            <Typography variant="h3">
              <b>WiFi Terms and Conditions</b>
            </Typography>
          </Box>
          <Typography>
            <b>Introduction:</b> document governs service; consent to WiFi
            document: implied; consent to WiFi terms and conditions: express;
            service user minimum age.
          </Typography>
          <Typography>
            <b>Rights to use WiFi service</b>: means of access to service;
            purpose of use of service; operating a "fair use" policy;
            restricting access to service.
          </Typography>
          <Typography>
            <b>Acceptable use:</b> acceptable use of WiFi: prohibitions.
          </Typography>
          <Typography>
            <b>Signing up:</b> registering for an account with service;
            information provided to be accurate; no other person permitted to
            use service; using other person's device to access service;
            acknowledgement of possible automatic connection to service.
          </Typography>
          <Typography>
            <b>Cancellation and suspension of access:</b> suspension or
            cancellation of access to service.
          </Typography>
          <Typography>
            <b>Your content: licence:</b> definition of user content
            (transmission); licence of user content for service; sub-licensing
            of user content.
          </Typography>
          <Typography>
            <b>Your content: rules:</b> defining "your content"; user content
            warranty; no unlawful user content; user content rules; transmission
            of material which has been the subject of previous complaints.
          </Typography>
          <Typography>
            <b>Limited warranties:</b> no warranties that service will be
            available; right to discontinue or alter service; no implied
            warranties or representations relating to service.
          </Typography>
          <Typography>
            <b>Limitations and exclusions of liability:</b> caveats to limits of
            liability; interpretation of limits of liability; no liability for
            loss or damage; no liability for force majeure; no liability for
            business losses; no liability for loss of data or software; no
            liability for consequential loss.
          </Typography>
          <Typography>
            <b>Indemnity:</b> indemnity from WiFi users.
          </Typography>
          <Typography>
            <b>Breaches of these terms and conditions:</b> consequences of
            breach; non-circumvention of suspension or prohibition.
          </Typography>
          <Typography>
            <b>Third party services:</b> using the service to access third party
            services; no control or liability for third party websites and
            services.
          </Typography>
          <Typography>
            <b>Variation:</b> document may be revised; variation of WiFi
            document; variation of WiFi document: registered users.
          </Typography>
          <Typography>
            <b>Assignment:</b> assignment by first party.
          </Typography>
          <Typography>
            <b>Severability:</b> severability of whole; severability of parts.
          </Typography>
          <Typography>
            <b>Third party rights:</b> third party rights: benefit; third party
            rights: exercise of rights.
          </Typography>
          <Typography>
            <b>Entire agreement:</b> entire agreement for use of service.
          </Typography>
          <Typography>
            <b>Law and jurisdiction:</b> governing law; jurisdiction.
          </Typography>
        </Box>
      </Container>
    </div>
  );
}

export default TermsConditionsPage;
